<?php
    include 'init.php';
    $account = $_POST['account'];
    $password = $_POST['password'];
    $sql_Query = "select * from account where acc_user = '$account' and password = '$password' Limit 1";
    $objQuery = mysqli_query($conn,$sql_Query);
    if(mysqli_fetch_array($objQuery)){
        $arr['user'] = $account;
        $arr['success'] = "true";
        echo json_encode($arr,JSON_UNESCAPED_UNICODE);
        exit();
    }
    else{
        $sql_Query = "select * from account where acc_user = 'account' limit 1";
        $objQuery = mysqli_query($conn,$sql_Query);
        if(mysqli_fetch_array($objQuery)){
            $arr['user'] = "密碼錯誤，請從新輸入";
            $arr['success'] = "false";
            echo json_encode($arr,JSON_UNESCAPED_UNICODE);
            exit();
        }
        else{
            $arr['user'] = "此帳號尚未註冊";
            $arr['success'] = "false";
            echo json_encode($arr,JSON_UNESCAPED_UNICODE);
            exit();
        }
    }
?>