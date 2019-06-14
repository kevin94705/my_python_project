<?php
    include 'init.php';
    $account = $_POST['account'];
    $password = $_POST['password'];
    $email = $_POST['email'];

    /**** Check account ****/

    $sql_Query = "select * from account where acc_user = '$account'";
    $objQuery = mysqli_query($conn,$sql_Query);
    if(mysqli_fetch_array($objQuery))
    {
        $arr['Error'] = "帳號已存在";
        $arr['Jump'] = "false";
        echo json_encode($arr, JSON_UNESCAPED_UNICODE);
        exit();
    }
    else{
        /**** Check account ****/
        $sql_Query = "select * from account where mail = '$email'";
        $objQuery = mysqli_query($conn,$sql_Query);
        if(mysqli_fetch_array($objQuery))
        {
            $arr['Error'] = "E-mail已存在";
            $arr['Jump'] = "false";
            echo json_encode($arr,JSON_UNESCAPED_UNICODE);
            exit();
        }
        else{
            /**** Insert ****/

            $sql_Query = "insert into account (acc_user,password,mail) values ('$account','$password','$email')";
            if(mysqli_query($conn,$sql_Query)){
                    $arr['Error'] = "創建帳號成功";
                    $arr['Jump'] = "true";
                    echo json_encode($arr,JSON_UNESCAPED_UNICODE);
                    echo 'Data Submit Successfully ！';
                    exit();
            }
            else{
                $arr['Error'] = "請檢查連線狀態";
                $arr['Jump'] = "false";
                echo json_encode($arr,JSON_UNESCAPED_UNICODE);
                echo 'Try Again';
                exit();
            }
            mysqli_close($conn);
        }
    }
?>