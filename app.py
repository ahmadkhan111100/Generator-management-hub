<meta name="csrf-token" content="F88P6YX09M6PysBQ7RiCs440DA38bknRF7zlCZEh" />
<!--<link href="https://v12.softsuitetech.com/assets/css/select2.min.css" rel="stylesheet" />-->

<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css" rel="stylesheet" />
    <meta charset="utf-8" />
    <link rel="apple-touch-icon" sizes="76x76" href="https://v12.softsuitetech.com/paper/img/apple-icon.png">
    <link rel="icon" type="image/png" href="https://v12.softsuitetech.compaper/img/favicon.png">
<!--<link href="https://v12.softsuitetech.com/assets/css/select2.min.css" rel="stylesheet" />-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<!--<link rel="stylesheet" type="text/css" href="https://v12.softsuitetech.com/assets/css/dataTables.bootstrap4.css">-->
    <link rel="stylesheet" type="text/css" href="https://v12.softsuitetech.com/assets/css/responsive.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<!--<script type="" src="https://v12.softsuitetech.com/assets/js/select2.full.min.js"></script>-->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/buttons/1.6.4/css/buttons.dataTables.min.css">
    <!-- Canonical SEO -->
    <link rel="canonical" href="" />
    <!--  Social tags      -->
    <meta name="keywords" content="">
    <meta name="description" content="">
    <!-- Schema.org markup for Google+ -->
    <meta itemprop="name" content="">
    <meta itemprop="description" content="">

    <meta itemprop="image" content="">
    <title>
        Generators
    </title>
    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no'
          name='viewport' />
    <!--     Fonts and icons     -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700,200" rel="stylesheet" />
    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css" rel="stylesheet">
    <!-- CSS Files -->
    <link href="https://v12.softsuitetech.com/paper/css/bootstrap.min.css" rel="stylesheet" />
    <link href="https://v12.softsuitetech.com/paper/css/paper-dashboard.css?v=2.0.0" rel="stylesheet" />
    <CSS Just for demo purpose, don't include it in your project -->
    <link href="https://v12.softsuitetech.com/paper/demo/demo.css" rel="stylesheet" />
    <style type="text/css">
        .card .card-body {
            padding: 0px 15px 10px 15px !important;
    }
        .sidebar .sidebar-wrapper, .off-canvas-sidebar .sidebar-wrapper {
            position: relative;
            height: calc(100vh - 75px);
            overflow: auto;
            width: auto;
            z-index: 4;
            padding-bottom: 100px;
        }
        .main-panel{
            width: auto;
        }
        .sidenav {
            height: 100%;
            width: 0;
            position: fixed;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: #111;
            overflow-x: hidden;
            transition: 0.5s;
            padding-top: 60px;
        }

        .sidenav a {
            padding: 8px 8px 8px 32px;
            text-decoration: none;
            font-size: 25px;
            color: #818181;
            display: block;
            transition: 0.3s;
        }

        .sidenav a:hover {
            color: #f1f1f1;
        }

        .sidenav .closebtn {
            position: absolute;
            top: 0;
            right: 25px;
            font-size: 36px;
            margin-left: 50px;
        }

        body {
            overflow-x: hidden;
            font-size:13px;
        }
        #sidebar-wrapper {
            min-height: 100vh;
            margin-left: -15rem;
            -webkit-transition: margin .25s ease-out;
            -moz-transition: margin .25s ease-out;
            -o-transition: margin .25s ease-out;
            transition: margin .25s ease-out;
        }
        .customMargin
        {
            margin-top: -5px;
        }
        #sidebar-wrapper .sidebar-heading {
            padding: 0.875rem 1.25rem;
            font-size: 1.2rem;
        }
        #sidebar-wrapper .list-group {
            width: 15rem;
        }
        #page-content-wrapper {
            min-width: 100vw;
        }
        #wrapper.toggled #sidebar-wrapper {
            margin-left: 0;
        }
        @media (min-width: 768px) {
            #sidebar-wrapper {
                margin-left: 0;
            }
            #page-content-wrapper {
                min-width: 0;
                width: 100%;
            }
            #wrapper.toggled #sidebar-wrapper {
                margin-left: -15rem;
            }
        }
        .loader {
            border: 16px solid #f3f3f3;
            border-radius: 50%;
            border-top: 16px solid #3498db;
            width: 120px;
            height: 120px;
            -webkit-animation: spin 2s linear infinite; /* Safari */
            animation: spin 2s linear infinite;
        }
        /* Safari */
        @-webkit-keyframes spin {
            0% { -webkit-transform: rotate(0deg); }
            100% { -webkit-transform: rotate(360deg); }
        }

        @keyframes  spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        @media  screen and (max-height: 450px) {
            .sidenav {padding-top: 15px;}
            .sidenav a {font-size: 18px;}
        }
        .wrapper{
            display:none;
        }
        .table>thead>tr>th, .table>tbody>tr>th, .table>tfoot>tr>th, .table>thead>tr>td, .table>tbody>tr>td, .table>tfoot>tr>td {
            font-size: 10px !important;
        }
        .sidebar .nav p, .off-canvas-sidebar .nav p {
    margin-bottom: -5px;
}
.sidebar .nav li>a, .off-canvas-sidebar .nav li>a {

    color:white;
}
    </style>
    <!-- Google Tag Manager -->
    <style>
     input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
        -webkit-appearance: none;
        margin: 0;
    }
     input[type=number] {
        -moz-appearance: textfield;
    }
        @media(max-width:600px) {
            #mySidenav {
                width: 345px !important;
                padding-left: 87px !important;
            }
            #openNav{
                display:none !important;
            }
            .main-panel{
                width:100% !important;
            }
            .sidebar, .bootstrap-navbar {
                left: -86px;
            }
        }
     .sidebar[data-active-color="danger"] .nav li.active>a, .sidebar[data-active-color="danger"] .nav li.active>a i, .sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"], .sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"] i, .sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"]~div>ul>li.active .sidebar-mini-icon, .sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"]~div>ul>li.active>a, .off-canvas-sidebar[data-active-color="danger"] .nav li.active>a, .off-canvas-sidebar[data-active-color="danger"] .nav li.active>a i, .off-canvas-sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"], .off-canvas-sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"] i, .off-canvas-sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"]~div>ul>li.active .sidebar-mini-icon, .off-canvas-sidebar[data-active-color="danger"] .nav li.active>a[data-toggle="collapse"]~div>ul>li.active>a {
         color:coral;
     }
     
     .main-panel {
        background: lightgray !important;    
     }
