-- MySQL dump 10.16  Distrib 10.1.21-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: localhost
-- ------------------------------------------------------
-- Server version	10.1.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `iset_agent`
--

DROP TABLE IF EXISTS `iset_agent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_agent` (
  `idx_agent` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `idx_agentname` bigint(20) unsigned NOT NULL DEFAULT '1',
  `id_agent` varbinary(512) DEFAULT NULL,
  `enabled` int(10) unsigned DEFAULT '1',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_agent`),
  UNIQUE KEY `id_agent` (`id_agent`),
  KEY `idx_agentname` (`idx_agentname`),
  CONSTRAINT `iset_agent_ibfk_1` FOREIGN KEY (`idx_agentname`) REFERENCES `iset_agentname` (`idx_agentname`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_agent`
--

LOCK TABLES `iset_agent` WRITE;
/*!40000 ALTER TABLE `iset_agent` DISABLE KEYS */;
INSERT INTO `iset_agent` VALUES (1,1,'_SYSTEM_RESERVED_',1,'2017-02-05 19:19:36','2017-02-05 19:19:36'),(2,2,'e33ce6311cf95c6264c6777323e9c717220b19ccad7b6da1877384e7fb3364e7',1,'2017-02-05 19:28:13','2017-02-05 19:28:13'),(3,2,'bec9ba91e14804001e037fa4f52c94fb1ef027d04e1b86f6a74ab36e3b073609',1,'2017-02-06 22:41:40','2017-02-06 22:41:40'),(4,3,'56a59077490e87ac40cccb8b11eea5527990daa1dcfbaa86fcb17be4f83b094d',1,'2017-04-10 09:46:03','2017-04-10 09:46:03');
/*!40000 ALTER TABLE `iset_agent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iset_agentname`
--

DROP TABLE IF EXISTS `iset_agentname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_agentname` (
  `idx_agentname` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varbinary(512) DEFAULT NULL,
  `enabled` int(10) unsigned DEFAULT '1',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_agentname`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_agentname`
--

LOCK TABLES `iset_agentname` WRITE;
/*!40000 ALTER TABLE `iset_agentname` DISABLE KEYS */;
INSERT INTO `iset_agentname` VALUES (1,'_SYSTEM_RESERVED_',1,'2017-02-05 19:19:36','2017-02-05 19:19:36'),(2,'DoRoad',1,'2017-02-05 19:28:13','2017-02-05 19:28:13'),(3,'_garnet',1,'2017-04-10 09:46:03','2017-04-10 09:46:03');
/*!40000 ALTER TABLE `iset_agentname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iset_billcode`
--

DROP TABLE IF EXISTS `iset_billcode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_billcode` (
  `idx_billcode` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `code` varbinary(512) DEFAULT NULL,
  `name` varbinary(512) DEFAULT NULL,
  `enabled` int(10) unsigned DEFAULT '1',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_billcode`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_billcode`
--

LOCK TABLES `iset_billcode` WRITE;
/*!40000 ALTER TABLE `iset_billcode` DISABLE KEYS */;
INSERT INTO `iset_billcode` VALUES (1,'_SYSTEM_RESERVED_','_SYSTEM_RESERVED_',1,'2017-02-05 19:19:36','2017-02-05 19:19:36');
/*!40000 ALTER TABLE `iset_billcode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iset_configuration`
--

DROP TABLE IF EXISTS `iset_configuration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_configuration` (
  `idx_configuration` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `config_key` varbinary(512) DEFAULT NULL,
  `config_value` varbinary(512) DEFAULT NULL,
  `enabled` int(10) unsigned DEFAULT '1',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_configuration`),
  UNIQUE KEY `config_key` (`config_key`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_configuration`
--

LOCK TABLES `iset_configuration` WRITE;
/*!40000 ALTER TABLE `iset_configuration` DISABLE KEYS */;
INSERT INTO `iset_configuration` VALUES (1,'version','0.0.0.0',1,'2017-02-05 19:19:36','2017-02-05 19:19:36');
/*!40000 ALTER TABLE `iset_configuration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iset_data`
--

DROP TABLE IF EXISTS `iset_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_data` (
  `idx_datapoint` bigint(20) unsigned NOT NULL DEFAULT '1',
  `timestamp` bigint(20) unsigned NOT NULL,
  `value` float DEFAULT NULL,
  PRIMARY KEY (`idx_datapoint`,`timestamp`),
  CONSTRAINT `iset_data_ibfk_1` FOREIGN KEY (`idx_datapoint`) REFERENCES `iset_datapoint` (`idx_datapoint`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_data`
--

LOCK TABLES `iset_data` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `iset_datapoint`
--

DROP TABLE IF EXISTS `iset_datapoint`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_datapoint` (
  `idx_datapoint` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `idx_deviceagent` bigint(20) unsigned NOT NULL DEFAULT '1',
  `idx_department` bigint(20) unsigned NOT NULL DEFAULT '1',
  `idx_billcode` bigint(20) unsigned NOT NULL DEFAULT '1',
  `id_datapoint` varbinary(512) DEFAULT NULL,
  `agent_label` varbinary(512) DEFAULT NULL,
  `agent_source` varbinary(512) DEFAULT NULL,
  `enabled` int(10) unsigned DEFAULT '1',
  `billable` int(10) unsigned DEFAULT '0',
  `timefixed_value` varbinary(512) DEFAULT NULL,
  `base_type` int(10) unsigned DEFAULT '1',
  `last_timestamp` bigint(20) unsigned NOT NULL DEFAULT '0',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_datapoint`),
  UNIQUE KEY `id_datapoint` (`id_datapoint`),
  KEY `idx_deviceagent` (`idx_deviceagent`),
  KEY `idx_department` (`idx_department`),
  KEY `idx_billcode` (`idx_billcode`),
  CONSTRAINT `iset_datapoint_ibfk_1` FOREIGN KEY (`idx_deviceagent`) REFERENCES `iset_deviceagent` (`idx_deviceagent`),
  CONSTRAINT `iset_datapoint_ibfk_2` FOREIGN KEY (`idx_department`) REFERENCES `iset_department` (`idx_department`),
  CONSTRAINT `iset_datapoint_ibfk_3` FOREIGN KEY (`idx_billcode`) REFERENCES `iset_billcode` (`idx_billcode`)
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_datapoint`
--

LOCK TABLES `iset_datapoint` WRITE;
/*!40000 ALTER TABLE `iset_datapoint` DISABLE KEYS */;
INSERT INTO `iset_datapoint` VALUES (1,1,1,1,'_SYSTEM_RESERVED_','_SYSTEM_RESERVED_','_SYSTEM_RESERVED_',1,0,NULL,1,0,'2017-02-05 19:19:36','2017-02-05 19:19:36');
/*!40000 ALTER TABLE `iset_datapoint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iset_department`
--

DROP TABLE IF EXISTS `iset_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_department` (
  `idx_department` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `code` varbinary(512) DEFAULT NULL,
  `name` varbinary(512) DEFAULT NULL,
  `enabled` int(10) unsigned DEFAULT '1',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_department`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_department`
--

LOCK TABLES `iset_department` WRITE;
/*!40000 ALTER TABLE `iset_department` DISABLE KEYS */;
INSERT INTO `iset_department` VALUES (1,'_SYSTEM_RESERVED_','_SYSTEM_RESERVED_',1,'2017-02-05 19:19:36','2017-02-05 19:19:36');
/*!40000 ALTER TABLE `iset_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iset_device`
--

DROP TABLE IF EXISTS `iset_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_device` (
  `idx_device` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `devicename` varbinary(512) DEFAULT NULL,
  `description` varbinary(512) DEFAULT NULL,
  `enabled` int(10) unsigned DEFAULT '1',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_device`),
  UNIQUE KEY `devicename` (`devicename`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_device`
--

LOCK TABLES `iset_device` WRITE;
/*!40000 ALTER TABLE `iset_device` DISABLE KEYS */;
INSERT INTO `iset_device` VALUES (1,'_SYSTEM_RESERVED_','_SYSTEM_RESERVED_',1,'2017-02-05 19:19:36','2017-02-05 19:19:36'),(2,'+1 876-927-1680',NULL,1,'2017-02-05 19:28:13','2017-02-05 19:28:13'),(3,'+1 876-927-1660',NULL,1,'2017-02-06 22:41:40','2017-02-06 22:41:40'),(4,'localhost.localdomain',NULL,1,'2017-04-10 09:46:03','2017-04-10 09:46:03');
/*!40000 ALTER TABLE `iset_device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iset_deviceagent`
--

DROP TABLE IF EXISTS `iset_deviceagent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iset_deviceagent` (
  `idx_deviceagent` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `idx_device` bigint(20) unsigned NOT NULL DEFAULT '1',
  `idx_agent` bigint(20) unsigned NOT NULL DEFAULT '1',
  `enabled` int(10) unsigned DEFAULT '1',
  `last_timestamp` bigint(20) unsigned NOT NULL DEFAULT '0',
  `ts_modified` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ts_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idx_deviceagent`),
  UNIQUE KEY `idx_device` (`idx_device`,`idx_agent`),
  KEY `idx_agent` (`idx_agent`),
  CONSTRAINT `iset_deviceagent_ibfk_1` FOREIGN KEY (`idx_device`) REFERENCES `iset_device` (`idx_device`),
  CONSTRAINT `iset_deviceagent_ibfk_2` FOREIGN KEY (`idx_agent`) REFERENCES `iset_agent` (`idx_agent`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iset_deviceagent`
--

LOCK TABLES `iset_deviceagent` WRITE;
/*!40000 ALTER TABLE `iset_deviceagent` DISABLE KEYS */;
INSERT INTO `iset_deviceagent` VALUES (1,1,1,1,0,'2017-02-05 19:19:36','2017-02-05 19:19:36'),(2,2,2,1,0,'2017-02-06 22:47:11','2017-02-05 19:28:13'),(3,3,3,1,0,'2017-02-06 22:47:11','2017-02-06 22:41:40'),(4,4,4,1,0,'2017-04-10 09:46:03','2017-04-10 09:46:03');
/*!40000 ALTER TABLE `iset_deviceagent` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-29 18:09:57