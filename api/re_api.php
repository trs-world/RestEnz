<?php
$selectName = $_GET['name'];
$enzymeJson = file_get_contents('restriction_enzymes.json');
$enzymeJson = mb_convert_encoding($enzymeJson, 'UTF8', 'ASCII,JIS,UTF-8,EUC-JP,SJIS-WIN');
$obj = json_decode($enzymeJson, true);
$resultNum = array_search($selectName, array_column($obj, 'name'));
if($resultNum != False) {
	$result = $obj[$resultNum];
    echo json_encode($result);
}
else {
	$result = array('name' => 'Not Invalid');
	echo json_encode(($result));
}
?>