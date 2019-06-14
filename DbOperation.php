       
<?php
    include 'init.php';
    $id = $_GET['id'];

    $sql_Query = "SELECT * FROM platrecoder WHERE id = '$id'";
    $result = mysqli_query($conn,$sql_Query ) or die('MySQL query error');
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