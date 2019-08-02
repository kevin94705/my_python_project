<?php
    require 'PHPMailer.php';
    require 'SMTP.php';
    require 'Exception.php';
    include 'init.php';

    $email = $_POST['email'];
    $sql = "select * from account where mail = '$email'";
    $result = mysqli_query($conn,$sql) or die('MySQL query error');
    if(!mysqli_fetch_array($result))
    {
        $arr['Error'] = "帳號不存在";
        echo json_encode($arr, JSON_UNESCAPED_UNICODE);
        exit();
    }
    else{
        $C_message = "www";
        
        $mail= new PHPMailer\PHPMailer\PHPMailer(); //建立新物件   

        $mail->IsSMTP(); //設定SMTP需要驗證   

        $mail->CharSet = "utf-8";                       //郵件編碼
        $mail->Host = "smtp.gmail.com";             //Gamil的SMTP主機
        $mail->SMTPDebug = 1;
        $mail->Port = 465;                                 //Gamil的SMTP主機的埠號(Gmail為465)。

        $mail->SMTPSecure = 'ssl';  
        $mail->SMTPAuth = true; 
        $mail->IsHTML(true);                             //郵件內容為html
    
        $mail->Username = "cx3500cx@gmail.com";       //Gamil帳號
        $mail->Password = "0925193935";                 //Gmail密碼

        $mail->From = ("cx3500cx@gmail.com");        //寄件者信箱
        $mail->AddAddress($email);
        $mail->Subject ="忘記密碼"; //郵件標題
        $mail->Body = "親愛的 '$email'，您好：<br />回應內容:'$C_message'"; //郵件內容

        if($mail->Send()){
            echo "信件已送出";
            exit();
        }else{
            echo "信件未送出";
            exit();
        }
    }
	mysqli_close($conn);
?>