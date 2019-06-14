<?php
    include 'init.php';
    /**** Check connection db ****/

    $ras_time = $_GET['id'];
    $temperture = $_GET['temperture'];
    $water = $_GET['water'];
    $light = $_GET['light'];
    $water_level = $_GET['water_level'];

    /* get value by get */
    $sql_Query = "insert into platrecoder (id,temperture,water,lightlevel,water_level) values('$ras_time','$temperture','$water','$light','$water_level')";
    if(mysqli_query($conn,$sql_Query)){
        echo 'insert data Successfully';
    }
    mysqli_close($conn);
?>