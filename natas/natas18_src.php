<?
$maxid = 640; // 640 should be enough for everyone

function createID($user) { 
    global $maxid;
    return rand(1, $maxid);
}

function my_session_start() { 
    if(array_key_exists("PHPSESSID", $_COOKIE) and is_numeric($_COOKIE["PHPSESSID"])) {
        if(session_start()) {
            if(!array_key_exists("admin", $_SESSION)) {
                $_SESSION["admin"] = 0; // backwards compatible, secure
            }
            return true;
        } else {
            return false;
        }
    }
    return false;
}

function print_credentials() { 
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
        print "You are an admin. The credentials for the next level are:<br>";
        print "<pre>Username: natas19\n";
        print "Password: <censored></pre>";
    } else {
        print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}


$showform = true;
if(my_session_start()) {
    print_credentials();
    $showform = false;
} else {
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
        session_id(rand(1, $maxid));
        session_start();
        $_SESSION["admin"] = 0;
        $showform = false;
        print_credentials();
    }
}  
?>