CREATE DATABASE  IF NOT EXISTS `appointmentsdb` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `appointmentsdb`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: appointmentsdb
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task` varchar(255) NOT NULL,
  `date` datetime NOT NULL,
  `status` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_appointments_users_idx` (`user_id`),
  CONSTRAINT `fk_appointments_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (2,'Music rehearsal','2022-08-12 00:00:00','Missed','2022-08-27 15:25:08','2022-08-27 15:25:08',1),(3,'Visit Kia Motors','2022-08-16 00:00:00','Done','2022-08-27 15:25:48','2022-08-27 15:25:48',1),(4,'Doctor\'s appointment','2022-08-02 00:00:00','Pending','2022-08-27 15:28:44','2022-08-27 15:55:13',1),(5,'Take Fifi to doctor','2022-08-27 00:00:00','Pending','2022-08-27 15:55:42','2022-08-27 15:55:42',1),(6,'make breakfast','2022-08-17 00:00:00','Missed','2022-08-27 16:06:00','2022-08-27 16:06:00',1),(7,'play guitar','2022-08-18 00:00:00','Missed','2022-08-27 16:12:00','2022-08-27 16:12:00',2),(8,'clean appartment','2022-08-10 00:00:00','Done','2022-08-27 16:12:52','2022-08-27 16:12:52',2),(9,'visit Pichincha volcano','2022-08-26 00:00:00','Pending','2022-08-27 16:13:31','2022-08-27 16:13:31',2),(10,'take guitar to workshop','2022-08-29 00:00:00','Pending','2022-08-27 16:17:46','2022-08-27 16:17:46',2),(11,'take jobo for a walk','2022-08-28 00:00:00','Pending','2022-08-27 16:23:39','2022-08-27 16:23:39',3),(12,'buy groceries','2022-08-29 00:00:00','Pending','2022-08-27 16:24:08','2022-08-27 16:24:08',3),(13,'buy a chocolate icecream for mom','2022-08-30 00:00:00','Pending','2022-08-27 16:26:31','2022-08-27 16:26:31',1);
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-27 12:10:50
