<?php
$servername = "RDS-Endpoint";
$username = "Your Username";
$password = "Password";
$dbname = "Database Name";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM employees";
$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html>
<head>
    <title>My Dynamic Web Page</title>
</head>
<body>
    <h1>Employee Data from RDS</h1>
<?php
    if ($result->num_rows > 0) {
        echo "<table border='1'><tr>";
        while ($fieldinfo = $result->fetch_field()) {
            echo "<th>{$fieldinfo->name}</th>";
        }
        echo "</tr>";

        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            foreach($row as $cell){
                echo "<td>$cell</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No records found.";
    }
?>
</body>
</html>
