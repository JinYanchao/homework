-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: emaildb
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `h_email`
--

DROP TABLE IF EXISTS `h_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `h_email` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(50) DEFAULT NULL,
  `receiver` varchar(50) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `context` varchar(1000) DEFAULT NULL,
  `p_date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `h_email`
--

LOCK TABLES `h_email` WRITE;
/*!40000 ALTER TABLE `h_email` DISABLE KEYS */;
INSERT INTO `h_email` VALUES (1,'jin884411@163.com','jycwork@outlook.com','测试','这是一段文字，用于测试邮件客户端是否好用。\n','2019-05-08 19:46:42'),(2,'jin884411@163.com','jycwork@outlook.com','测试','这是一段文字，用于测试邮件客户端是否好用。\n\n','2019-05-08 19:56:21'),(4,'jin884411@163.com','jycwork@outlook.com','测试','这是一段文字，用于测试邮件客户端是否好用。\n\n\n','2019-05-08 21:16:56'),(5,'jin884411@163.com','yanchao.jin@outlook.com','测试2','用于测试\n','2019-05-09 13:08:33'),(6,'jin884411@163.com','yanchao.jin@outlook.com','测试2','用于测试\n','2019-05-09 13:08:34'),(7,'jin884411@163.com','yanchao.jin@outlook.com','测试2','用于测试\n','2019-05-09 13:08:34'),(8,'jin884411@163.com','yanchao.jin@outlook.com','测试2','用于测试\n','2019-05-09 13:08:36');
/*!40000 ALTER TABLE `h_email` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-09 13:32:57
