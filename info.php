<?php
    include 'init.php';
    $sql = "SELECT * FROM `platrecoder` WHERE 1";
    $result = mysqli_query($conn,$sql) or die('MySQL query error');
    while($row = mysqli_fetch_array($result)){
        $data_array[] = array(
            "id" => $row['id'],            
			"temperture" => $row['temperture'],
			"water" => $row['water'],
			"light" =>$row['lightlevel'],
		);
    }
	echo json_encode($data_array);
	mysqli_close($conn);
?>