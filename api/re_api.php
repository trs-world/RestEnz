<?php
$enzymeJson = file_get_contents('restriction_enzymes.json');
$obj = json_decode($enzymeJson, true); //string => arrayへ変換する
$resultNum = array_search($_GET['name'], array_column($obj, 'name')); //arrayから検索する
if($resultNum != False) {
    echo json_encode($obj[$resultNum]);
}
else {
	echo json_encode(array('name' => 'Not Invalid'));
}
?>
