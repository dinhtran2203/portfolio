<?php
    /* For more information of email to form:
        https://html.form.guide/email-form/html-email-form/
        https://html.form.guide/email-form/php-form-to-email/
    */
    
    if (!isset($_POST['submit']))
    {
        echo "error; you need to submit form!";
    }

    $name = $_POST['name'];
    $visitor_email = $_POST['email'];
    $message = $_POST['message'];

    $email_from = 'dinh2203@gmail.com';
    $email_subject = 'Contract from portfolio';
    $email_body = "Message from $name.\n". 
        "Here is the message: \n $message".

    $to = 'dinh2203@gmail.com';
    $headers = "From: $email_from \r\n";
    mail($to, $email_subject, $email_body, $headers)
?>