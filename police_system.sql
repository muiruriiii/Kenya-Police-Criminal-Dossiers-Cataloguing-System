-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 01, 2023 at 01:30 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `police_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add citizen', 7, 'add_citizen'),
(26, 'Can change citizen', 7, 'change_citizen'),
(27, 'Can delete citizen', 7, 'delete_citizen'),
(28, 'Can view citizen', 7, 'view_citizen'),
(29, 'Can add crime list', 8, 'add_crimelist'),
(30, 'Can change crime list', 8, 'change_crimelist'),
(31, 'Can delete crime list', 8, 'delete_crimelist'),
(32, 'Can view crime list', 8, 'view_crimelist'),
(33, 'Can add criminal', 9, 'add_criminal'),
(34, 'Can change criminal', 9, 'change_criminal'),
(35, 'Can delete criminal', 9, 'delete_criminal'),
(36, 'Can view criminal', 9, 'view_criminal'),
(37, 'Can add officer', 10, 'add_officer'),
(38, 'Can change officer', 10, 'change_officer'),
(39, 'Can delete officer', 10, 'delete_officer'),
(40, 'Can view officer', 10, 'view_officer'),
(41, 'Can add crime', 11, 'add_crime'),
(42, 'Can change crime', 11, 'change_crime'),
(43, 'Can delete crime', 11, 'delete_crime'),
(44, 'Can view crime', 11, 'view_crime'),
(45, 'Can add crime anonymous', 12, 'add_crimeanonymous'),
(46, 'Can change crime anonymous', 12, 'change_crimeanonymous'),
(47, 'Can delete crime anonymous', 12, 'delete_crimeanonymous'),
(48, 'Can view crime anonymous', 12, 'view_crimeanonymous'),
(49, 'Can add evidence', 13, 'add_evidence'),
(50, 'Can change evidence', 13, 'change_evidence'),
(51, 'Can delete evidence', 13, 'delete_evidence'),
(52, 'Can view evidence', 13, 'view_evidence'),
(53, 'Can add ob', 14, 'add_ob'),
(54, 'Can change ob', 14, 'change_ob'),
(55, 'Can delete ob', 14, 'delete_ob'),
(56, 'Can view ob', 14, 'view_ob'),
(57, 'Can add police station', 15, 'add_policestation'),
(58, 'Can change police station', 15, 'change_policestation'),
(59, 'Can delete police station', 15, 'delete_policestation'),
(60, 'Can view police station', 15, 'view_policestation'),
(61, 'Can add case', 16, 'add_case'),
(62, 'Can change case', 16, 'change_case'),
(63, 'Can delete case', 16, 'delete_case'),
(64, 'Can view case', 16, 'view_case');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(16, 'records', 'case'),
(7, 'records', 'citizen'),
(11, 'records', 'crime'),
(12, 'records', 'crimeanonymous'),
(8, 'records', 'crimelist'),
(9, 'records', 'criminal'),
(13, 'records', 'evidence'),
(14, 'records', 'ob'),
(10, 'records', 'officer'),
(15, 'records', 'policestation'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-06-19 19:21:39.701152'),
(2, 'auth', '0001_initial', '2022-06-19 19:21:44.417565'),
(3, 'admin', '0001_initial', '2022-06-19 19:21:45.443295'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-06-19 19:21:45.484265'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-06-19 19:21:45.515478'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-06-19 19:21:46.006397'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-06-19 19:21:46.955896'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-06-19 19:21:47.079220'),
(9, 'auth', '0004_alter_user_username_opts', '2022-06-19 19:21:47.141748'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-06-19 19:21:47.411986'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-06-19 19:21:47.427761'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-06-19 19:21:47.537053'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-06-19 19:21:47.659479'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-06-19 19:21:47.721909'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-06-19 19:21:47.785534'),
(16, 'auth', '0011_update_proxy_permissions', '2022-06-19 19:21:47.801158'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-06-19 19:21:47.848084'),
(18, 'sessions', '0001_initial', '2022-06-19 19:21:48.029961'),
(19, 'records', '0001_initial', '2022-07-14 14:11:19.917599'),
(20, 'records', '0002_alter_crime_table', '2022-07-14 14:43:17.084589'),
(21, 'records', '0003_crimeanonymous_crime_reportdate_alter_crime_crimeid', '2022-07-18 11:47:54.839653'),
(22, 'records', '0004_evidence_ob_rename_reportdate_crime_reporttime', '2022-07-18 11:47:54.849629'),
(23, 'records', '0005_crime_hasob_alter_ob_table', '2022-07-18 11:47:54.855269'),
(24, 'records', '0002_alter_crime_hasob', '2022-07-18 12:30:54.630325'),
(25, 'records', '0003_alter_crime_hasob', '2022-07-18 12:42:52.881595');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0buvy7qc58h05o2y4nvsgoftu58m6gzt', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTczNzMzNjIuOTAzMzU3fQ:1oAAWQ:JeuVQzLU4Z3exWuhWqCVmYtV2Lse_vU9K8jn2p1Gr6E', '2022-07-09 13:34:22.932360'),
('14499skmtw4dpxa71h4zsazo05rfno7a', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNzU0MjEuNTYzNDIzfQ:1o9L1p:hmoi_YAkCGVD3ngenyEYuy6YbwrEG3neCRbnJ1S6xyo', '2022-07-07 06:35:21.588436'),
('17j8uj3woxk4ff67h7u2cgd4syb6wjc2', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTc0Mzg0ODcuMzE3NTcxOSwib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1oARSt:t2qO4bQPEtO85ID1sFbOmkXZSfqb2VeB_BOcX86cPak', '2022-07-10 07:39:51.540826'),
('2pkrv1l2bk4szgxl15u7ikwpd581owh9', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNDQ3NzkuNTA4MzQ2LCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIiwib2ZmaWNlcklEIjoxfQ:1o9D4T:0i1j8k5UtqCjtC3OGTQogavMrzKGpC1nNSrsDIqdT3k', '2022-07-06 22:05:33.759833'),
('344hcrxvb1io838frmww4w2t3q6i4hh2', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTc0MzczOTIuNTIxODU0OSwib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1oARBI:YKwRfaqbcM1meyrlB_IuCTBGyqIFXb8jNt3lbiUNn5A', '2022-07-10 07:21:40.146411'),
('3q2572f033qwx9jz63yydx9ot1yrx8iq', '.eJxFjrsOgkAQRX-FTI0guz4ILTZaaCL2mwkOMOo-4q6Nxn93jUTKe0_u4wXKk_dsjWLDQQXW5ANqp6AqVsv1QpblXGZSirKQKdiu45bue9QEFezsYJKNJUih5cBPMiOofyo5xa4JbjX2X5o_3M3i2eejPxMiu7ge_vVNwBAfxQfT5BHNNWYPdQPvD26IPBs:1oExBz:A13ssZ-b95Tin4pTSR0WdbhafQtZz6-ZiNd4OrrrwbQ', '2022-08-05 18:16:03.758469'),
('4r08p5qhanimcx25mkjuqnu7rs0jxshn', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTczNzA5NjkuMjk2NDQyfQ:1oA9tp:0p2nKB_VaP9p1ySiWMAMS81fZCesMC1H1nrR79PepnM', '2022-07-09 12:54:29.317654'),
('5cpf9coq2s0263omjzh7hjbpivd0n6ve', '.eJyrVspPS8tMTi0KLkksyczPU7IyNNeBifkl5qYqWSkFpSZVKXgn5mXmZSrpKMUXpxYXA1XGA7kl8SWZuanFJYm5BfFAnWamFkbm5kYGJnqmlmaGZoYWtQAyaB9X:1oDxn7:d-XdEB7VL1weDuMVzXzeBuT9N5jVqEK8Ns15a6y0fA0', '2022-08-03 00:42:17.637176'),
('5gnisxt296ib26wbe1txecd86qpfjgug', '.eJxFzrEOgjAUheFXIXdGaDFIZWbBxM5uTcWCF2xvtTVGje-uJkTX8w3nf4IKJgQkp9BhVBGtCVFbr6Dmq7KqGGMFz0ohuFiuU6C-x85cpLYGatjQ0SUNGUihw4gP42aQI02YbG_aDfjH1urhq_nVn0gfQj7vi4Ipv7vL856y0Q_wu2mbT8XrDYsmNqI:1oD6jp:tZzuxcSJWTt91lkZ7wrgfYhjeA7WE7AShBjK11kUhwA', '2022-07-31 16:03:21.212109'),
('6lxi11hvsuudf901huhc8ktiulhhd2q0', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTczNzAzMzEuMTQwMzQ2NSwib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1oA9jg:ldCuZP9Hkp-kYQ1y13UzW3ZmTsP-a2FQGNwfYcls9G8', '2022-07-09 12:44:00.638889'),
('843g96zfrmb25xcelpi9ik3b0o0gvdjf', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNDU5OTcuMDUzNjg5LCJvZmZpY2VySUQiOjEsIm9mZmljZXJOYW1lIjoiSm9obiBEb2UifQ:1o9DNH:e9pB9yQiFWHp1sx65qYyKqN1lMNNFh46RsSj4O0BSwA', '2022-07-06 22:24:59.340696'),
('8d4dekr2kfrlitmaiv8sobjusjjrcl7h', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTczNzI3MDIuOTk1NDUxN30:1oAALn:ngZY4fnixgtj5da4MHoSJSOhTmWacqOtq3VMTbSCckQ', '2022-07-09 13:23:23.062455'),
('ai68852reikzkij0fylkv0j702n2pcq5', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNzQ5ODAuMTMyOTM3Nywib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1o9Kui:qSZx0KoL2aIXlHuwGkpLKFpv2aKw9gVbswWEKItXzRQ', '2022-07-07 06:28:00.443066'),
('aw44gpz22qcdmjoh26k0i7tk3aikfvig', '.eJyrVspPS8tMTi3ydFGyMjTVgXGDSxJLMvPzgGLmcDG_xNxUJSuloNSkKgXvxLzMvEwlHaX44tTiYqDKeCC3JL4kMze1uCQxtyAeqNPM1MLI3NzU0kDP0tzYwtLctBYAB2Qj5g:1oDxkk:9BMZ0Y9xReQgOvUkuTjrBdA7AA97eFigHFXEylynGHY', '2022-08-03 00:39:50.985906'),
('bn4jlz6jo461tz3vy5lg9ap6zmels91k', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTc0MzY2NTguMDA3MDMsIm9mZmljZXJJRCI6MSwib2ZmaWNlck5hbWUiOiJKb2huIERvZSJ9:1oAQzO:w2zWk3aCW05QasPnSdSIY-jRQUYrsDBqmCgSszPHZW8', '2022-07-10 07:09:22.123504'),
('gafh5k1we12rqquoi1607ru685q9tg4t', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTc0MzcwMTQuNzY4OTEwMiwib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1oAR58:_RnnaN3GZRrU5QqzyWUBkqmhqJ1tdeHR0Gf42CTUHYU', '2022-07-10 07:15:18.125581'),
('gx117hi4o1ww74a6k6d9lqnmqki7m45v', 'eyJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIiwiX3Nlc3Npb25faW5pdF90aW1lc3RhbXBfIjoxNjU3MzYyNjkzLjg5NjUyNzMsIm9mZmljZXJJRCI6MX0:1oA7mJ:r_6OCSPaqZwA3b7Lm7HFkaADZkWLMo6f6zwqsXUCNj4', '2022-07-09 10:38:35.392888'),
('kb8cufftdf5pz9fw3g1blsltxeb1e1rv', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTczNzE3MDEuNjQxMjA5MX0:1oAA5d:jjvmMx33CpBI3S8iOFdCvuWuN_TVUTK5hhT7FGrsscU', '2022-07-09 13:06:41.662206'),
('kdky73frf11ss1mcmeey67u1ssehfwmk', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTc0MzYxMDUuNDc1OTAyOCwib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1oAQqS:TpKw7MOp7m-lctGw_X7MUTp-eLjlHCr9-Bp4t-_RCEI', '2022-07-10 07:00:08.896951'),
('mv3digbv3owglgqpdnqrhg2zs9ddne48', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNDQ0NTIuNTEzMzY5Niwib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4ifQ:1o9CyN:Z_lXmFANTgULSqD74lgAMLr7MA1JyPaOwBqAzEaZG7c', '2022-07-06 21:59:15.389558'),
('q7a9vkttapmqagkiscimvu1bvfhrnd4x', 'eyJvZmZpY2VySUQiOjEsIm9mZmljZXJOYW1lIjoiSm9obiIsIl9zZXNzaW9uX2luaXRfdGltZXN0YW1wXyI6MTY1NzE0NDEzOC4zNzc2ODAzfQ:1o9CtG:gmb8mPyF268cKf4OmiYzeNeexnoWFsk61G8BoomYVaI', '2022-07-06 21:53:58.390052'),
('qyqf3bzwzba83w0pso26l9m6sdx0d3x7', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNDUxNzQuNzg0ODE3Nywib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1o9DA2:uqyY1IEV761ZnOAa2q2MBhiePLxSZLVD91YLwFRYKLs', '2022-07-06 22:11:18.441869'),
('vr528i0npdu1v9fhihuyx1wfbsar0mah', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTczNzM0MzguNzM1NjcwMywib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1oAAXp:jREpcEzIYPzyjMtPJMGWxWpgqK8AyGbFGHmWoQMN970', '2022-07-09 13:35:49.025054'),
('vr8nygprrq4d38076wo26vb47fk6pryz', 'eyJvZmZpY2VySUQiOjEsIm9mZmljZXJOYW1lIjoiSm9obiBEb2UiLCJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTc2OTg0MzIuOTk0NjM1OH0:1oBX5V:XTXg2c_pTJVbL3j-Wr4oWG6nLkUDrBoXY3zhphKCn1E', '2022-07-27 07:47:13.011650'),
('wmtx7418eizgg9eer606a82ag6me5yia', '.eJw9jkEOgjAQRa9CZo1gAal2KxtcYCIHaBocsGpbQseNxrtbI7L8783k_xd0mvQTbaMMgoAKjYsaT5Mi7SzEf10bNXx9-hjvTp19OvNVxpLrOIRD6dH78CO11SRJG_SkzChBsLLkuzzPtuukKDacMx6D63vd4VRXQS_ppOwtdBz3LSyspd8SwfKFzVsP7mKjyiG8PxWBQXA:1osTeR:t6f3YqshR9QDOvEjfW-_s490KgpiecMqZIk3-T6fd1w', '2022-11-22 18:48:47.793623'),
('x0s2beqouarodeltuzn627bkjbrlqnor', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNDY1MzAuODQ3Mjg5M30:1o9DVq:9T2WNQhm7L65cH2MFZhTvbvtjPobE3a2TNw9bEmOjC0', '2022-07-06 22:33:50.856290'),
('y88ur609608mt78md3bnwzj3jf1ax8hd', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTczNjk4MjYuNDUyOTY5Mywib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1oA9bU:PM-op_84y0jsSfAL7-qQPQR7z3UjASSQMBgjTdp7_28', '2022-07-09 12:35:32.707938'),
('yp2c0npej3tgt5lp99ysgdaeuhd5xfff', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE2NTcxNDU1MDIuMzMxMDY0NSwib2ZmaWNlcklEIjoxLCJvZmZpY2VyTmFtZSI6IkpvaG4gRG9lIn0:1o9DFL:53wuNrPX8KABzMXqIDvBHlb1B_s6Y-xkL8dgrs4VIG0', '2022-07-06 22:16:47.169252'),
('ys7go56zcgae7poi2g44yk9jn6pj6qoy', '.eJyrVkrOLMmsSs3zS8xNVbJS8srPyFPSUcpPS8tMTi3CKujpomRlqKMUX5xaXJyZnxefmZdZEl-SmZtaXJKYWxAPlDQzNTc2NbI0MNUzMrQwNzE2qwUADqkhPQ:1oA5CT:UeS57PcySWS0e1lg7Ek_5Mgnq0IeuY5npODRIayS030', '2022-07-09 07:53:25.296747');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_accident_abstract`
--

CREATE TABLE `tbl_accident_abstract` (
  `aaID` int(6) NOT NULL,
  `reportDate` datetime NOT NULL,
  `officerID` int(6) NOT NULL,
  `accidentLocation` varchar(40) NOT NULL,
  `vehicleID` varchar(40) NOT NULL,
  `accidentDate` int(10) NOT NULL,
  `trafficChargeRegNo` int(10) NOT NULL,
  `investigatingOfficerID` int(10) NOT NULL,
  `witnessID` int(10) NOT NULL,
  `officerinchargerID` int(10) NOT NULL,
  `isDeleted` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_admin`
--

CREATE TABLE `tbl_admin` (
  `adminID` int(6) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `tel` varchar(40) NOT NULL,
  `password` varchar(120) NOT NULL,
  `nationalId` int(10) NOT NULL,
  `isDeleted` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_case`
--

CREATE TABLE `tbl_case` (
  `id` int(6) NOT NULL,
  `officerID` int(6) NOT NULL,
  `obID` int(6) NOT NULL,
  `previousStation` int(6) DEFAULT NULL,
  `currentStation` int(6) NOT NULL,
  `caseStatus` enum('PENDING','APPROVED','SOLVED','UNSOLVED','REJECTED') NOT NULL DEFAULT 'PENDING',
  `generateDate` datetime NOT NULL DEFAULT current_timestamp(),
  `caseNumber` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_case`
--

INSERT INTO `tbl_case` (`id`, `officerID`, `obID`, `previousStation`, `currentStation`, `caseStatus`, `generateDate`, `caseNumber`) VALUES
(1, 1, 49, 13, 17, 'APPROVED', '2022-07-19 17:00:18', 'CSF-1-2022-07-19 20:00:18.141436'),
(2, 1, 51, 13, 18, 'APPROVED', '2022-07-19 20:28:28', 'CSF-2-2022-07-19 23:28:28.175578'),
(3, 1, 52, 13, 18, 'APPROVED', '2022-07-19 23:04:46', 'CSF-3-2022-07-20 02:04:46.469523'),
(4, 1, 50, 13, 17, 'PENDING', '2022-07-20 00:35:00', 'CSF-4-2022-07-20 03:35:00.934398'),
(5, 1, 53, 13, 18, 'APPROVED', '2022-07-22 07:51:54', 'CSF-5-2022-07-22 10:51:54.053713'),
(6, 1, 54, NULL, 13, 'APPROVED', '2022-07-22 09:58:57', 'CSF-6-2022-07-22 12:58:57.618076');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_citizen`
--

CREATE TABLE `tbl_citizen` (
  `id` int(6) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `tel` varchar(40) NOT NULL,
  `password` varchar(120) NOT NULL,
  `nationalID` int(10) NOT NULL,
  `gender` enum('Male','Female') NOT NULL,
  `address` varchar(40) NOT NULL,
  `citizenImage` varchar(40) NOT NULL,
  `accountStatus` tinyint(1) NOT NULL DEFAULT 0,
  `joinDate` datetime NOT NULL DEFAULT current_timestamp(),
  `isDeleted` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_citizen`
--

INSERT INTO `tbl_citizen` (`id`, `fName`, `lName`, `email`, `tel`, `password`, `nationalID`, `gender`, `address`, `citizenImage`, `accountStatus`, `joinDate`, `isDeleted`) VALUES
(15, 'Mkay', 'Joe', 'mraynjan@gmail.com', '0792881712', 'pbkdf2_sha256$320000$izoBYQkVhT92P2W5YFtpZ6$JsJXp9VX9m6KbPGKNNEKWppCwUPiLKlyRz3yH4JDMDY=', 37610988, 'Female', 'Kisumu', 'citizen-15.jpg', 0, '2022-07-13 16:14:25', 0),
(19, 'Danroy', 'Ndung\'u', 'danroyndungu@gmail.com', '+254727143069', 'pbkdf2_sha256$320000$rZOwNizy36vLIFFoNa1M8L$k5RUc9M3tUhH49IrDQ7ikSDoCvmsWcn8BG9AzuTpcB8=', 39395240, 'Male', 'Lang\'ata,Nairobi', 'citizen-19_qtEsNsk.jpg', 0, '2022-07-14 13:43:11', 0),
(20, 'Njoki', 'Mwangi', 'rebecca.muiruri@strathmore.edu', '254709176652', 'pbkdf2_sha256$320000$o8SASY9EoG1IpEXXYu3rdr$WPDZ8k9w9cju1ru+YJhXRGufmH3ZDF7Kj05JVrW8+bs=', 31720977, 'Female', 'Ruaka', 'citizen-20_pXyNqbo.jpg', 0, '2022-07-17 13:50:48', 0),
(21, 'Demo', 'Nstration', 'danroy@gmail.com', '0727143069', 'pbkdf2_sha256$320000$1QyJEDWjjI0Rg3S7A2XYiS$zYXTDkK9cneT///Rnef5d/d1vfDw5zsG6p2G4KtQf3g=', 39395240, 'Male', 'Kakamega', 'citizen-21.jpg', 0, '2022-07-22 07:34:21', 0),
(22, 'Citizen', 'Test', 'citizen@gmail.com', '0727143069', 'pbkdf2_sha256$320000$l3uVfXqFQ4guS5UlI5GcKg$m8iRCmv16k09+Kqjkvy7AhErtZxVtVPzzbi+pk+skgA=', 39395240, 'Male', 'Nairobi', 'citizen-22.jpg', 0, '2022-07-22 09:47:16', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_crimelist`
--

CREATE TABLE `tbl_crimelist` (
  `crimeID` int(8) NOT NULL,
  `crimeName` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_crimelist`
--

INSERT INTO `tbl_crimelist` (`crimeID`, `crimeName`) VALUES
(1, 'Theft'),
(2, 'Rape'),
(3, 'Sexual Assault'),
(4, 'Physical Assault'),
(5, 'Accident'),
(8, 'Others'),
(9, 'Embezzlement'),
(10, 'Murder');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_crime_report`
--

CREATE TABLE `tbl_crime_report` (
  `id` int(6) NOT NULL,
  `description` varchar(400) NOT NULL,
  `crimeID` int(6) NOT NULL,
  `citizenID` int(6) NOT NULL,
  `isdeleted` tinyint(1) NOT NULL DEFAULT 0,
  `reportTime` datetime NOT NULL DEFAULT current_timestamp(),
  `hasOB` int(11) NOT NULL DEFAULT 0,
  `files` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_crime_report`
--

INSERT INTO `tbl_crime_report` (`id`, `description`, `crimeID`, `citizenID`, `isdeleted`, `reportTime`, `hasOB`, `files`) VALUES
(1, 'My watch was stolen.', 1, 19, 0, '2022-07-18 12:04:05', 49, ''),
(2, 'My watch was stolen.', 1, 19, 0, '2022-07-18 12:04:05', 50, ''),
(4, 'Happened along ngong rd at 8pm', 4, 20, 0, '2022-07-18 12:04:05', 51, ''),
(8, 'Milk was stolen from kitchen.', 1, 19, 0, '2022-07-19 22:23:15', 52, '\"[\\\"CRA-8-0.jpg\\\", \\\"CRA-8-1.jpg\\\", \\\"CRA-8-2.jpg\\\", \\\"CRA-8-3.mp4\\\"]\"'),
(9, 'Thugs stole my laptop around Nairobi West on Thursday 20 July 2022', 1, 21, 0, '2022-07-22 07:35:59', 53, '\"[\\\"CRA-9-0.jpg\\\", \\\"CRA-9-1.jpg\\\", \\\"CRA-9-2.jpeg\\\"]\"'),
(10, 'Assaulted along Mbagathi.', 4, 22, 0, '2022-07-22 09:48:16', 54, '\"[\\\"CRA-10-0.jpg\\\", \\\"CRA-10-1.jpg\\\"]\"');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_crime_report_anonymous`
--

CREATE TABLE `tbl_crime_report_anonymous` (
  `id` int(6) NOT NULL,
  `description` varchar(400) NOT NULL,
  `crimeID` int(6) NOT NULL,
  `isdeleted` tinyint(1) NOT NULL DEFAULT 0,
  `reportTime` datetime NOT NULL DEFAULT current_timestamp(),
  `hasOB` tinyint(1) NOT NULL DEFAULT 0,
  `files` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`files`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_crime_report_anonymous`
--

INSERT INTO `tbl_crime_report_anonymous` (`id`, `description`, `crimeID`, `isdeleted`, `reportTime`, `hasOB`, `files`) VALUES
(20, 'Milk was stolen in the kitchen.', 1, 0, '2022-07-19 22:17:17', 0, '\"[\\\"CRA-20-0.jpg\\\", \\\"CRA-20-1.jpg\\\", \\\"CRA-20-2.jpg\\\", \\\"CRA-20-3.MOV\\\"]\"'),
(21, 'Along Ngong Rd', 4, 0, '2022-07-20 00:43:19', 0, '\"[\\\"CRA-21-0.png\\\"]\"'),
(22, 'Assaulted by a police officer.', 4, 0, '2022-07-22 07:33:21', 0, '\"[\\\"CRA-22-0.png\\\"]\"'),
(23, 'Car crashed into an electric post.', 5, 0, '2022-07-22 07:36:35', 0, '\"[]\"'),
(24, 'My car was stolen in Lang\'ata.', 1, 0, '2022-07-22 09:46:18', 0, '\"[]\"'),
(25, 'Companies stealing money.', 9, 0, '2022-07-22 09:48:32', 0, '\"[]\"');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_criminal`
--

CREATE TABLE `tbl_criminal` (
  `id` int(6) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `tel` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `crimeID` int(6) NOT NULL,
  `criminalStatus` enum('PENDING','APPROVED','REJECTED') NOT NULL,
  `locationArrest` varchar(20) NOT NULL,
  `nationalID` varchar(20) NOT NULL,
  `address` varchar(40) NOT NULL,
  `criminalImage` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `dateAdded` datetime NOT NULL DEFAULT current_timestamp(),
  `isDeleted` tinyint(1) NOT NULL DEFAULT 0,
  `arrestDate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_criminal`
--

INSERT INTO `tbl_criminal` (`id`, `fName`, `lName`, `tel`, `gender`, `crimeID`, `criminalStatus`, `locationArrest`, `nationalID`, `address`, `criminalImage`, `dateAdded`, `isDeleted`, `arrestDate`) VALUES
(1, 'Jam', 'The Cat', '+254727143069', 'male', 8, 'APPROVED', 'Utawala', '098765', 'Utawala, Nairobi', '\"[\\\"Criminal-1-0.jpg\\\", \\\"Criminal-1-1.jpg\\\", \\\"Criminal-1-2.jpg\\\"]\"', '2022-07-20 02:02:23', 0, '2022-07-19 23:02:23'),
(2, 'Criminal', 'Crime', '0731242345', 'male', 9, 'APPROVED', 'Ruai', '39395240', 'Ruai', '\"[\\\"Criminal-2-0.png\\\", \\\"Criminal-2-1.png\\\", \\\"Criminal-2-2.webp\\\"]\"', '2022-07-22 10:53:01', 0, '2022-07-22 07:53:01'),
(3, 'Assualter', 'Crime', '0731242345', 'male', 10, 'APPROVED', 'Mbagathi', '39395240', 'Mbagathi', '\"[\\\"Criminal-3-0.jpg\\\", \\\"Criminal-3-1.jpg\\\", \\\"Criminal-3-2.jpg\\\"]\"', '2022-07-22 12:51:48', 0, '2022-07-22 09:51:48');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_doctor`
--

CREATE TABLE `tbl_doctor` (
  `doctorID` int(6) NOT NULL,
  `hospitalID` int(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_evidence`
--

CREATE TABLE `tbl_evidence` (
  `id` int(6) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `Form` varchar(40) NOT NULL,
  `evidenceFiles` varchar(40) DEFAULT NULL,
  `isDeleted` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_evidence`
--

INSERT INTO `tbl_evidence` (`id`, `description`, `Form`, `evidenceFiles`, `isDeleted`) VALUES
(1, 'content', '', '', 0),
(2, 'wow', '', '', 0),
(3, 'dgcubuy', '', '', 0),
(4, 'v  gvvyh', '', '', 0),
(5, 'lmao', '', '', 0),
(6, 'koko', '', '', 0),
(7, 'lop', '', '', 0),
(8, 'rred', '', '', 0),
(9, 'rewq', '', 'evidence-9.jpg', 0),
(10, 'redse', '', 'evidence-10.jpg', 0),
(11, 'sad', '', 'evidence-11.jpg', 0),
(12, 'rewqooi', '', 'evidence-12.jpg', 0),
(13, 'put', '', 'evidence-13.jpg', 0),
(14, 'poiuyrew', 'form-14.pdf', 'form-14.pdf', 0),
(15, 'uytrewryui', 'form-15.pdf', 'evidence-15.jpg', 0),
(16, 'uwixvshbcj', 'form-16.pdf', 'evidence-16.jpg', 0),
(17, 'dsdfgiuyfgh', 'form-17.pdf', 'evidence-17.jpg', 0),
(18, 'jhdfghujioiuyt', 'form-18.pdf', 'evidence-18.jpg', 0),
(19, 'suyvc ehccs', 'form-19.pdf', 'evidence-19.jpg', 0),
(20, 'nhhfcfg', 'form-20.pdf', 'evidence-20.jpg', 0),
(21, 'upload evidence', 'form-21.pdf', 'evidence-21.jpg', 0);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_hospital`
--

CREATE TABLE `tbl_hospital` (
  `hospitalID` int(6) NOT NULL,
  `location` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_insurance`
--

CREATE TABLE `tbl_insurance` (
  `insuranceID` int(6) NOT NULL,
  `insuranceScheme` varchar(20) NOT NULL,
  `address` varchar(20) NOT NULL,
  `isDeleted` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_ob`
--

CREATE TABLE `tbl_ob` (
  `id` int(6) NOT NULL,
  `citizenID` int(6) NOT NULL,
  `crimeID` int(6) NOT NULL,
  `obNo` varchar(40) NOT NULL,
  `reportDate` datetime NOT NULL,
  `actionTaken` varchar(120) NOT NULL,
  `officerID` int(10) NOT NULL,
  `isDeleted` tinyint(1) DEFAULT 0,
  `createDate` datetime NOT NULL DEFAULT current_timestamp(),
  `file` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`file`)),
  `hasCase` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_ob`
--

INSERT INTO `tbl_ob` (`id`, `citizenID`, `crimeID`, `obNo`, `reportDate`, `actionTaken`, `officerID`, `isDeleted`, `createDate`, `file`, `hasCase`) VALUES
(49, 19, 1, '49/2022-07-18 16:22:01.393679/19', '2022-07-18 12:04:00', 'PUI', 1, 0, '2022-07-18 13:22:01', '\"[\\\"ob-49-1.png\\\", \\\"ob-49-2.pdf\\\"]\"', 1),
(50, 19, 1, '50/2022-07-19 20:06:14.287750/19', '2022-07-18 12:04:00', 'Investigating', 1, 0, '2022-07-19 17:06:14', NULL, 4),
(51, 20, 4, '51/2022-07-19 20:08:48.657882/20', '2022-07-18 12:04:00', 'PUI', 1, 0, '2022-07-19 17:08:48', NULL, 2),
(52, 19, 1, '52/2022-07-20 02:03:00.306764/19', '2022-07-19 22:23:00', 'Cat Under Investigation', 1, 0, '2022-07-19 23:03:00', NULL, 3),
(53, 21, 1, '53/2022-07-22 10:51:28.728763/21', '2022-07-22 07:35:00', 'PUI', 1, 0, '2022-07-22 07:51:28', '\"[\\\"ob-53-1.png\\\"]\"', 5),
(54, 22, 4, '54/2022-07-22 12:58:46.634569/22', '2022-07-22 09:48:00', 'PUI', 1, 0, '2022-07-22 09:58:46', '\"[\\\"ob-54-1.pdf\\\", \\\"ob-54-2.pdf\\\"]\"', 6);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_p3`
--

CREATE TABLE `tbl_p3` (
  `p3ID` int(6) NOT NULL,
  `citizenID` int(6) NOT NULL,
  `dateReported` varchar(20) NOT NULL,
  `hospitalID` int(6) NOT NULL,
  `crimeLocation` varchar(40) NOT NULL,
  `caseID` int(6) NOT NULL,
  `officerID` int(6) NOT NULL,
  `crimeID` int(6) NOT NULL,
  `isDeleted` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_police_officer`
--

CREATE TABLE `tbl_police_officer` (
  `id` int(6) NOT NULL,
  `fName` varchar(20) NOT NULL,
  `lName` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `tel` varchar(40) NOT NULL,
  `password` varchar(120) NOT NULL,
  `nationalId` int(10) NOT NULL,
  `gender` enum('male','female') NOT NULL,
  `address` varchar(80) NOT NULL,
  `employmentDate` datetime NOT NULL DEFAULT current_timestamp(),
  `employmentStatus` int(2) NOT NULL DEFAULT 0,
  `rank` varchar(10) NOT NULL,
  `isDeleted` tinyint(1) NOT NULL DEFAULT 0,
  `stationID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_police_officer`
--

INSERT INTO `tbl_police_officer` (`id`, `fName`, `lName`, `email`, `tel`, `password`, `nationalId`, `gender`, `address`, `employmentDate`, `employmentStatus`, `rank`, `isDeleted`, `stationID`) VALUES
(1, 'John', 'Doe', 'police@gmail.com', '234567987', 'pbkdf2_sha256$320000$U3I9qChUrtJiiMg2FACjFM$tOnqVnVc7Y/gjX2sCpXVtFE7d3DLgQu4A2FSiXAno5k=', 39395240, 'male', 'Ukambani', '2022-07-01 15:37:38', 0, 'OCS', 0, 13),
(15, 'Rebz', 'Kanini', 'rebz@gmail.com', '12345678', 'pbkdf2_sha256$320000$dDSjSBnYP0jmzTS14DxSyW$/j/ca9eSSy2Ly5MUcaGKSB13z17d/l5m9qFrQAGFDdY=', 12345678, 'female', 'Kenya', '2022-07-04 12:30:37', 0, 'Constable', 0, 17),
(16, 'Trevor', 'Anto', 'trevor@gmail.com', '12345', 'pbkdf2_sha256$320000$oIr0cLkG3FAjQUUEVpKRkb$8pYHncuYk/RbSD46kxf5J50qLbn80ib/jO/PoyNFqv0=', 213456, 'male', 'Ruai,Nairobi', '2022-07-04 13:01:16', 0, 'Constable', 0, 13),
(18, 'New', 'Officer', 'new@gmail.com', '0727143069', 'pbkdf2_sha256$320000$NxOG328syJRpynD6Un1qED$PsD6XrtJhQLI0VdI/mJzF98l5ogHmLK4sB3iXlTJSV4=', 39395240, 'male', 'Ruai', '2022-07-22 07:49:52', 0, 'Constable', 0, 18),
(19, 'John', 'Mwangi', 'mwas@gmail.com', '07551263623', 'pbkdf2_sha256$320000$Th6AJHxBGGfdz4CPcAYGGx$Ew9jvtMs67p2L8R01t8daAh/9hSdYQOTEN5kMRRSb9U=', 39395240, 'male', 'Kamulu', '2022-07-22 07:50:48', 0, 'Constable', 0, 17),
(20, 'Police', 'Rebz', 'rebecca@police.com', '+254727143069', 'pbkdf2_sha256$320000$jemImfxkEN71BXPChdFvsy$jMgU7+1rjNfGUaOd80X7+FBI2PFgk/ellbvRLD+r3MY=', 34562859, 'female', 'Kiambu', '2022-07-22 07:58:11', 0, 'Constable', 0, 13),
(21, 'Police', 'Danroy', 'droy@gmail.com', '0727143069', 'pbkdf2_sha256$320000$VvXuA7TYodpObjvwI7doVL$L7PaBsrCuSUG8V2kdy/zMABTAonArkpwZ6hNnvN9P+s=', 39284827, 'male', 'Embakasi', '2022-07-22 08:00:30', 0, 'Constable', 0, 18),
(22, 'Officer', 'Test', 'officertest@gmail.com', '0727143069', 'pbkdf2_sha256$320000$GBMmIGvzV10WqVjhZiOzpj$9MKwQGNWGKpqKsxwgffWI4XFeb9D6jSfqC/N1uxXQaE=', 39284827, 'male', 'Nairobi', '2022-07-22 09:50:36', 0, 'Constable', 0, 19);

-- --------------------------------------------------------

--
-- Table structure for table `tbl_station`
--

CREATE TABLE `tbl_station` (
  `id` int(6) NOT NULL,
  `location` varchar(20) NOT NULL,
  `officersCount` varchar(20) NOT NULL,
  `address` varchar(40) NOT NULL,
  `ocsID` int(10) NOT NULL,
  `stationNumber` varchar(40) NOT NULL,
  `stationStatus` tinyint(1) NOT NULL DEFAULT 0,
  `establishDate` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_station`
--

INSERT INTO `tbl_station` (`id`, `location`, `officersCount`, `address`, `ocsID`, `stationNumber`, `stationStatus`, `establishDate`) VALUES
(13, 'Kiambu', '0', 'PO BOX Nai', 1, '13-Kiambu-2022-07-18 19:02:25.590112', 0, '2022-07-18 23:51:27'),
(17, 'Kamulu', '0', 'PO BOX Kamulu', 1, '17-Kamulu-2022-07-19 23:12:21.941286', 0, '2022-07-19 20:12:21'),
(18, 'Ruai', '0', 'PO BOX 44355', 1, '18-Ruai-2022-07-22 10:38:49.634876', 0, '2022-07-22 07:38:49'),
(19, 'Nakuru', '0', 'PO Box 4983', 1, '19-Nakuru-2022-07-22 12:50:00.622344', 0, '2022-07-22 09:50:00');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_vehicle`
--

CREATE TABLE `tbl_vehicle` (
  `vehicleID` int(6) NOT NULL,
  `vehicleMake` varchar(20) NOT NULL,
  `vehicleType` varchar(20) NOT NULL,
  `insuranceID` int(10) NOT NULL,
  `citizenID` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_witness`
--

CREATE TABLE `tbl_witness` (
  `witnessID` int(6) NOT NULL,
  `citizenID` int(6) NOT NULL,
  `caseID` int(10) NOT NULL,
  `stationID` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `tbl_accident_abstract`
--
ALTER TABLE `tbl_accident_abstract`
  ADD PRIMARY KEY (`aaID`),
  ADD KEY `investigatingOfficerID` (`investigatingOfficerID`),
  ADD KEY `officerinchargerID` (`officerinchargerID`),
  ADD KEY `witnessID` (`witnessID`);

--
-- Indexes for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  ADD PRIMARY KEY (`adminID`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `tbl_case`
--
ALTER TABLE `tbl_case`
  ADD PRIMARY KEY (`id`),
  ADD KEY `officerID` (`officerID`),
  ADD KEY `obID` (`obID`),
  ADD KEY `currentStation` (`currentStation`);

--
-- Indexes for table `tbl_citizen`
--
ALTER TABLE `tbl_citizen`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `tbl_crimelist`
--
ALTER TABLE `tbl_crimelist`
  ADD PRIMARY KEY (`crimeID`);

--
-- Indexes for table `tbl_crime_report`
--
ALTER TABLE `tbl_crime_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `crimeID` (`crimeID`),
  ADD KEY `citizenID` (`citizenID`);

--
-- Indexes for table `tbl_crime_report_anonymous`
--
ALTER TABLE `tbl_crime_report_anonymous`
  ADD PRIMARY KEY (`id`),
  ADD KEY `crimeID` (`crimeID`);

--
-- Indexes for table `tbl_criminal`
--
ALTER TABLE `tbl_criminal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `crimeID` (`crimeID`);

--
-- Indexes for table `tbl_doctor`
--
ALTER TABLE `tbl_doctor`
  ADD PRIMARY KEY (`doctorID`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `hospitalID` (`hospitalID`);

--
-- Indexes for table `tbl_evidence`
--
ALTER TABLE `tbl_evidence`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tbl_hospital`
--
ALTER TABLE `tbl_hospital`
  ADD PRIMARY KEY (`hospitalID`);

--
-- Indexes for table `tbl_insurance`
--
ALTER TABLE `tbl_insurance`
  ADD PRIMARY KEY (`insuranceID`);

--
-- Indexes for table `tbl_ob`
--
ALTER TABLE `tbl_ob`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `obNo` (`obNo`),
  ADD KEY `crimeID` (`crimeID`),
  ADD KEY `officerID` (`officerID`),
  ADD KEY `citizenID` (`citizenID`);

--
-- Indexes for table `tbl_p3`
--
ALTER TABLE `tbl_p3`
  ADD PRIMARY KEY (`p3ID`),
  ADD KEY `caseID` (`caseID`),
  ADD KEY `hospitalID` (`hospitalID`),
  ADD KEY `citizenID` (`citizenID`),
  ADD KEY `crimeID` (`crimeID`),
  ADD KEY `officerID` (`officerID`);

--
-- Indexes for table `tbl_police_officer`
--
ALTER TABLE `tbl_police_officer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `tbl_station`
--
ALTER TABLE `tbl_station`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `location` (`location`),
  ADD KEY `ocsID` (`ocsID`);

--
-- Indexes for table `tbl_vehicle`
--
ALTER TABLE `tbl_vehicle`
  ADD PRIMARY KEY (`vehicleID`),
  ADD KEY `insuranceID` (`insuranceID`),
  ADD KEY `citizenID` (`citizenID`);

--
-- Indexes for table `tbl_witness`
--
ALTER TABLE `tbl_witness`
  ADD PRIMARY KEY (`witnessID`),
  ADD KEY `citizenID` (`citizenID`),
  ADD KEY `caseID` (`caseID`),
  ADD KEY `stationID` (`stationID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `tbl_accident_abstract`
--
ALTER TABLE `tbl_accident_abstract`
  MODIFY `aaID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_admin`
--
ALTER TABLE `tbl_admin`
  MODIFY `adminID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_case`
--
ALTER TABLE `tbl_case`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tbl_citizen`
--
ALTER TABLE `tbl_citizen`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `tbl_crimelist`
--
ALTER TABLE `tbl_crimelist`
  MODIFY `crimeID` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tbl_crime_report`
--
ALTER TABLE `tbl_crime_report`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `tbl_crime_report_anonymous`
--
ALTER TABLE `tbl_crime_report_anonymous`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `tbl_criminal`
--
ALTER TABLE `tbl_criminal`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tbl_doctor`
--
ALTER TABLE `tbl_doctor`
  MODIFY `doctorID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_evidence`
--
ALTER TABLE `tbl_evidence`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `tbl_hospital`
--
ALTER TABLE `tbl_hospital`
  MODIFY `hospitalID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_insurance`
--
ALTER TABLE `tbl_insurance`
  MODIFY `insuranceID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_ob`
--
ALTER TABLE `tbl_ob`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `tbl_p3`
--
ALTER TABLE `tbl_p3`
  MODIFY `p3ID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_police_officer`
--
ALTER TABLE `tbl_police_officer`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `tbl_station`
--
ALTER TABLE `tbl_station`
  MODIFY `id` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `tbl_vehicle`
--
ALTER TABLE `tbl_vehicle`
  MODIFY `vehicleID` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbl_witness`
--
ALTER TABLE `tbl_witness`
  MODIFY `witnessID` int(6) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tbl_accident_abstract`
--
ALTER TABLE `tbl_accident_abstract`
  ADD CONSTRAINT `tbl_accident_abstract_ibfk_1` FOREIGN KEY (`investigatingOfficerID`) REFERENCES `tbl_police_officer` (`id`),
  ADD CONSTRAINT `tbl_accident_abstract_ibfk_2` FOREIGN KEY (`officerinchargerID`) REFERENCES `tbl_police_officer` (`id`),
  ADD CONSTRAINT `tbl_accident_abstract_ibfk_3` FOREIGN KEY (`witnessID`) REFERENCES `tbl_witness` (`witnessID`);

--
-- Constraints for table `tbl_case`
--
ALTER TABLE `tbl_case`
  ADD CONSTRAINT `tbl_case_ibfk_1` FOREIGN KEY (`officerID`) REFERENCES `tbl_police_officer` (`id`),
  ADD CONSTRAINT `tbl_case_ibfk_2` FOREIGN KEY (`obID`) REFERENCES `tbl_ob` (`id`),
  ADD CONSTRAINT `tbl_case_ibfk_3` FOREIGN KEY (`previousStation`) REFERENCES `tbl_station` (`id`),
  ADD CONSTRAINT `tbl_case_ibfk_4` FOREIGN KEY (`currentStation`) REFERENCES `tbl_station` (`id`);

--
-- Constraints for table `tbl_crime_report`
--
ALTER TABLE `tbl_crime_report`
  ADD CONSTRAINT `tbl_crime_report_ibfk_1` FOREIGN KEY (`crimeID`) REFERENCES `tbl_crimelist` (`crimeID`),
  ADD CONSTRAINT `tbl_crime_report_ibfk_2` FOREIGN KEY (`citizenID`) REFERENCES `tbl_citizen` (`id`);

--
-- Constraints for table `tbl_crime_report_anonymous`
--
ALTER TABLE `tbl_crime_report_anonymous`
  ADD CONSTRAINT `tbl_crime_report_anonymous_ibfk_1` FOREIGN KEY (`crimeID`) REFERENCES `tbl_crimelist` (`crimeID`);

--
-- Constraints for table `tbl_criminal`
--
ALTER TABLE `tbl_criminal`
  ADD CONSTRAINT `tbl_criminal_ibfk_1` FOREIGN KEY (`crimeID`) REFERENCES `tbl_crime_report` (`id`);

--
-- Constraints for table `tbl_doctor`
--
ALTER TABLE `tbl_doctor`
  ADD CONSTRAINT `tbl_doctor_ibfk_1` FOREIGN KEY (`hospitalID`) REFERENCES `tbl_hospital` (`hospitalID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
