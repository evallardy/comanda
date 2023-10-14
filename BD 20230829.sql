-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: comanda
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=182 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (77,'Can add log entry',1,'add_logentry'),(78,'Can change log entry',1,'change_logentry'),(79,'Can delete log entry',1,'delete_logentry'),(80,'Can view log entry',1,'view_logentry'),(81,'Can add permission',2,'add_permission'),(82,'Can change permission',2,'change_permission'),(83,'Can delete permission',2,'delete_permission'),(84,'Can view permission',2,'view_permission'),(85,'Can add group',3,'add_group'),(86,'Can change group',3,'change_group'),(87,'Can delete group',3,'delete_group'),(88,'Can view group',3,'view_group'),(89,'Can add content type',4,'add_contenttype'),(90,'Can change content type',4,'change_contenttype'),(91,'Can delete content type',4,'delete_contenttype'),(92,'Can view content type',4,'view_contenttype'),(93,'Can add session',5,'add_session'),(94,'Can change session',5,'change_session'),(95,'Can delete session',5,'delete_session'),(96,'Can view session',5,'view_session'),(97,'Can add Fecha de operación',6,'add_contable'),(98,'Can change Fecha de operación',6,'change_contable'),(99,'Can delete Fecha de operación',6,'delete_contable'),(100,'Can view Fecha de operación',6,'view_contable'),(101,'Cocina consulta',6,'cocina'),(102,'Cocina termina',6,'cocina_termina'),(103,'Cocina cancela',6,'cocina_cancela'),(104,'Bar consulta',6,'bar'),(105,'Bar termina',6,'bar_termina'),(106,'Bar cancela',6,'bar_cancela'),(107,'Comandas consulta',6,'servicio'),(108,'Comanda nueva',6,'servicio_nueva'),(109,'Comanda solicita',6,'servicio_solicitar'),(110,'Comanda cancela',6,'servicio_cancelar'),(111,'Comanda paga',6,'servicio_pagar'),(112,'Comanda detalle',6,'servicio_ver'),(113,'Comanda cierra',6,'servicio_cierra'),(114,'Entregas consulta',6,'entregas'),(115,'Entrega OK',6,'entregas_ok'),(116,'Entrega cancelada',6,'entregas_cancela'),(117,'Reasignar',6,'reasignar'),(118,'Consulta de seguimiento',6,'consultas_seguimiento'),(119,'Consulta de reporte del día',6,'consultas_reporte_dia'),(120,'Catálogo consulta',6,'catalogo'),(121,'Catálogo Agrega',6,'catalogo_agregar'),(122,'Catáogo Modifica',6,'catalogo_modificar'),(123,'Accesos consulta',6,'accesos'),(124,'Accesos modifica',6,'accesos_modificar'),(125,'Día abre',6,'abrir'),(126,'Día cierra',6,'cerrar'),(127,'Usuarios consulta',6,'usuarios'),(128,'Usuario nuevo',6,'crea_usuario'),(129,'Usuario modifica',6,'modifica_usuario'),(130,'Can add Comanda',7,'add_comanda'),(131,'Can change Comanda',7,'change_comanda'),(132,'Can delete Comanda',7,'delete_comanda'),(133,'Can view Comanda',7,'view_comanda'),(134,'Can add Detalle',8,'add_detalle'),(135,'Can change Detalle',8,'change_detalle'),(136,'Can delete Detalle',8,'delete_detalle'),(137,'Can view Detalle',8,'view_detalle'),(138,'Can add Producto',9,'add_producto'),(139,'Can change Producto',9,'change_producto'),(140,'Can delete Producto',9,'delete_producto'),(141,'Can view Producto',9,'view_producto'),(142,'Can add usuario',10,'add_usuario'),(143,'Can change usuario',10,'change_usuario'),(144,'Can delete usuario',10,'delete_usuario'),(145,'Can view usuario',10,'view_usuario'),(146,'Can add Promoción',11,'add_promocion'),(147,'Can change Promoción',11,'change_promocion'),(148,'Can delete Promoción',11,'delete_promocion'),(149,'Can view Promoción',11,'view_promocion'),(150,'Can add Escarcha',12,'add_escarcha'),(151,'Can change Escarcha',12,'change_escarcha'),(152,'Can delete Escarcha',12,'delete_escarcha'),(153,'Can view Escarcha',12,'view_escarcha'),(154,'Can add Complemento',13,'add_complemento'),(155,'Can change Complemento',13,'change_complemento'),(156,'Can delete Complemento',13,'delete_complemento'),(157,'Can view Complemento',13,'view_complemento'),(158,'Can add Cerveza',14,'add_cerveza'),(159,'Can change Cerveza',14,'change_cerveza'),(160,'Can delete Cerveza',14,'delete_cerveza'),(161,'Can view Cerveza',14,'view_cerveza'),(162,'Can add Carne',15,'add_carne'),(163,'Can change Carne',15,'change_carne'),(164,'Can delete Carne',15,'delete_carne'),(165,'Can view Carne',15,'view_carne'),(166,'Can add Sazonador',16,'add_sazona'),(167,'Can change Sazonador',16,'change_sazona'),(168,'Can delete Sazonador',16,'delete_sazona'),(169,'Can view Sazonador',16,'view_sazona'),(170,'Can add Producto',17,'add_promociondetalle'),(171,'Can change Producto',17,'change_promociondetalle'),(172,'Can delete Producto',17,'delete_promociondetalle'),(173,'Can view Producto',17,'view_promociondetalle'),(174,'Can add Promocion',18,'add_promocion'),(175,'Can change Promocion',18,'change_promocion'),(176,'Can delete Promocion',18,'delete_promocion'),(177,'Can view Promocion',18,'view_promocion'),(178,'Can add Grupo',19,'add_grupo'),(179,'Can change Grupo',19,'change_grupo'),(180,'Can delete Grupo',19,'delete_grupo'),(181,'Can view Grupo',19,'view_grupo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comanda`
--

DROP TABLE IF EXISTS `comanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comanda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `mesa` varchar(255) DEFAULT NULL,
  `observacion` varchar(255) DEFAULT NULL,
  `estatus` int NOT NULL,
  `fecha_contable` date NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `usuario_id` bigint DEFAULT NULL,
  `usuario_cancela_id` bigint DEFAULT NULL,
  `usuario_cierra_id` bigint DEFAULT NULL,
  `usuario_cliente_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Comanda_usuario_id_9efd87ac_fk_Usuario_id` (`usuario_id`),
  KEY `Comanda_usuario_cancela_id_93cc395f_fk_Usuario_id` (`usuario_cancela_id`),
  KEY `Comanda_usuario_cierra_id_7fa88f92_fk_Usuario_id` (`usuario_cierra_id`),
  KEY `Comanda_usuario_cliente_id_f0820fac_fk_Usuario_id` (`usuario_cliente_id`),
  CONSTRAINT `Comanda_usuario_cancela_id_93cc395f_fk_Usuario_id` FOREIGN KEY (`usuario_cancela_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Comanda_usuario_cierra_id_7fa88f92_fk_Usuario_id` FOREIGN KEY (`usuario_cierra_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Comanda_usuario_cliente_id_f0820fac_fk_Usuario_id` FOREIGN KEY (`usuario_cliente_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Comanda_usuario_id_9efd87ac_fk_Usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comanda`
--

LOCK TABLES `comanda` WRITE;
/*!40000 ALTER TABLE `comanda` DISABLE KEYS */;
/*!40000 ALTER TABLE `comanda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `complemento`
--

DROP TABLE IF EXISTS `complemento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `complemento` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `estatus` int NOT NULL,
  `tipo` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Complemento_tipo_nombre_427ce3c8_uniq` (`tipo`,`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `complemento`
--

LOCK TABLES `complemento` WRITE;
/*!40000 ALTER TABLE `complemento` DISABLE KEYS */;
INSERT INTO `complemento` VALUES (1,'Ajonjolí','2023-06-10 13:40:19.262073','2023-06-10 13:38:17.184816',1,4),(2,'Mora trueno pop','2023-06-10 13:40:42.593888','2023-06-10 13:40:42.593888',1,4),(3,'Bubaloo trueno pop','2023-06-10 13:40:53.222282','2023-06-10 13:40:53.222282',1,4),(4,'Súper miguelito','2023-06-17 00:00:53.997711','2023-06-10 13:41:04.706339',1,4),(5,'Dragoncito','2023-06-10 13:41:19.575666','2023-06-10 13:41:19.575666',1,4),(6,'Limoncito miguelito','2023-06-10 13:41:27.978009','2023-06-10 13:41:27.978009',1,4),(7,'Victoria','2023-06-17 01:02:29.222041','2023-06-17 01:02:29.222041',1,2),(8,'Corona','2023-06-17 01:03:38.563695','2023-06-17 01:03:38.563695',1,2),(9,'León','2023-06-17 01:04:14.152510','2023-06-17 01:03:58.400197',1,2),(10,'Modelo','2023-06-17 01:05:41.581781','2023-06-17 01:05:41.581781',1,2),(11,'Negra modelo','2023-06-17 01:07:06.942527','2023-06-17 01:07:06.942527',1,2),(12,'Heineken','2023-06-17 01:07:19.546310','2023-06-17 01:07:19.546310',1,2),(13,'Indio','2023-06-17 01:07:27.374399','2023-06-17 01:07:27.374399',1,2),(14,'XX Lager','2023-06-17 01:07:34.539042','2023-06-17 01:07:34.539042',1,2),(15,'XX Ambar','2023-06-17 01:07:43.123397','2023-06-17 01:07:43.123397',1,2),(16,'Budweisser','2023-06-17 01:07:50.983109','2023-06-17 01:07:50.983109',1,2),(17,'Miller','2023-06-17 01:07:58.208729','2023-06-17 01:07:58.208729',1,2),(18,'Ron','2023-06-17 15:04:09.689794','2023-06-17 15:04:09.689794',1,5),(19,'Sky vodka','2023-06-17 15:04:16.117369','2023-06-17 15:04:16.118375',1,5),(20,'Tequila','2023-06-17 15:04:22.766369','2023-06-17 15:04:22.766369',1,5),(21,'Vodka','2023-06-17 15:04:29.483057','2023-06-17 15:04:29.483057',1,5),(22,'Salsita de mango-piña','2023-06-17 15:05:01.490472','2023-06-17 15:05:01.490472',1,1),(23,'Salsita de fresa blueberry','2023-06-17 15:05:06.266545','2023-06-17 15:05:06.266545',1,1),(24,'Mezcal','2023-06-17 15:05:11.690280','2023-06-17 15:05:11.690280',1,1),(25,'Agua mineral','2023-06-17 15:05:51.627053','2023-06-17 15:05:51.627053',1,6),(26,'Crema de coco','2023-06-17 15:05:59.977720','2023-06-17 15:05:59.978719',1,6),(27,'Curacao azul','2023-06-17 15:06:06.931920','2023-06-17 15:06:06.932425',1,6),(28,'Gin','2023-06-17 15:06:13.437585','2023-06-17 15:06:13.437585',1,6),(29,'Jugo de limón','2023-06-17 15:06:24.587032','2023-06-17 15:06:24.587032',1,6),(30,'Jugo de naranja','2023-06-17 15:06:33.297508','2023-06-17 15:06:33.297508',1,6),(31,'Jugo de piña','2023-06-17 15:06:40.621843','2023-06-17 15:06:40.621843',1,6),(32,'Jugo de piña colada','2023-06-17 15:06:47.721933','2023-06-17 15:06:47.721933',1,6),(33,'Jugo de toronja','2023-06-17 15:06:53.974833','2023-06-17 15:06:53.974833',1,6),(34,'Licor de café','2023-06-17 15:07:00.100137','2023-06-17 15:07:00.100137',1,6),(35,'Licor de manzana verde','2023-06-17 15:07:05.908860','2023-06-17 15:07:05.908860',1,6),(36,'Licor de uva','2023-06-17 15:07:12.918364','2023-06-17 15:07:12.918364',1,6),(37,'Menta','2023-06-17 15:07:19.687873','2023-06-17 15:07:19.687873',1,6),(38,'Pepino','2023-06-17 15:07:28.454082','2023-06-17 15:07:28.454082',1,6),(39,'Receta especial','2023-06-17 15:07:34.766359','2023-06-17 15:07:34.766359',1,6),(41,'Sabor cítrico','2023-06-17 15:07:48.434786','2023-06-17 15:07:48.434786',1,6),(42,'Toque de la casa','2023-06-17 15:07:55.320668','2023-06-17 15:07:55.320668',1,6),(43,'Toque de rosas','2023-06-17 15:08:01.520611','2023-06-17 15:08:01.520611',1,6),(44,'Toque especial','2023-06-17 15:08:07.451636','2023-06-17 15:08:07.451636',1,6),(45,'Licor de mango piña','2023-06-17 15:08:14.442188','2023-06-17 15:08:14.442188',1,6),(46,'Licor de frutos rojos','2023-06-17 15:08:20.804581','2023-06-17 15:08:20.806180',1,6),(47,'Aderezo','2023-06-17 15:08:57.533303','2023-06-17 15:08:57.533303',1,8),(48,'Cebolla','2023-06-17 15:09:05.697382','2023-06-17 15:09:05.697382',1,8),(49,'Jalapeño','2023-06-17 15:09:13.007541','2023-06-17 15:09:13.007541',1,8),(50,'Jitomate','2023-06-17 15:09:19.842038','2023-06-17 15:09:19.842038',1,8),(51,'Tocino','2023-06-17 15:09:26.697496','2023-06-17 15:09:26.698493',1,8),(52,'Lechuga','2023-06-17 15:09:41.832179','2023-06-17 15:09:41.833179',1,8),(53,'Queso','2023-06-17 15:09:51.814959','2023-06-17 15:09:51.814959',1,8),(54,'Pollo','2023-06-17 15:10:05.841659','2023-06-17 15:10:05.841659',1,7),(55,'Res','2023-06-17 15:10:13.149251','2023-06-17 15:10:13.149251',1,7),(56,'Tamarindo natural','2023-06-17 15:11:13.951402','2023-06-17 15:11:13.951402',1,3),(57,'Pepino tamarindo','2023-06-17 15:11:21.234288','2023-06-17 15:11:21.234288',1,3),(58,'Mango crayón','2023-06-17 15:11:27.611248','2023-06-17 15:11:27.611248',1,3),(59,'Mora crayón','2023-06-17 15:11:33.706678','2023-06-17 15:11:33.706678',1,3),(60,'Uva crayón','2023-06-17 15:11:40.456817','2023-06-17 15:11:40.456817',1,3),(61,'Limon crayón','2023-06-17 15:11:46.080529','2023-06-17 15:11:46.080529',1,3),(62,'Bubaloo xtream','2023-06-17 15:11:53.343825','2023-06-17 15:11:53.343825',1,3),(63,'Brandy','2023-06-17 15:16:58.130170','2023-06-17 15:16:58.130170',1,5),(64,'Receta de la casa','2023-06-17 17:02:10.274541','2023-06-17 17:02:10.274541',1,1),(65,'Coca Cola','2023-06-22 23:19:36.489428','2023-06-22 23:19:36.489428',1,9),(66,'Ruffles flamming hot','2023-06-22 23:21:30.142091','2023-06-22 23:21:30.142091',1,10),(67,'Ruffles queso','2023-06-22 23:21:39.682039','2023-06-22 23:21:39.682039',1,10),(68,'Chetos bolitas','2023-06-22 23:21:47.429166','2023-06-22 23:21:47.429166',1,10),(69,'Chetos queso jalapeño','2023-06-22 23:21:59.688810','2023-06-22 23:21:59.688810',1,10),(70,'Naturales','2023-06-22 23:22:04.449791','2023-06-22 23:22:04.449791',1,1),(71,'Soda','2023-06-24 19:44:37.047903','2023-06-24 19:44:37.047903',1,9),(72,'Picosito','2023-06-25 02:43:50.977510','2023-06-25 02:43:50.977510',1,6),(73,'Mezcal','2023-06-25 02:52:42.001028','2023-06-25 02:52:42.001028',1,5);
/*!40000 ALTER TABLE `complemento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle`
--

DROP TABLE IF EXISTS `detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom_producto` varchar(255) DEFAULT NULL,
  `nota` varchar(255) NOT NULL,
  `especificacion` json DEFAULT NULL,
  `cantidad` int NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `importe` decimal(10,2) NOT NULL,
  `estatus` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `comanda_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  `usuario_id` bigint DEFAULT NULL,
  `usuario_cancela_id` bigint DEFAULT NULL,
  `usuario_cobra_id` bigint DEFAULT NULL,
  `usuario_elabora_id` bigint DEFAULT NULL,
  `usuario_entrega_id` bigint DEFAULT NULL,
  `usuario_reasigna_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Detalle_comanda_id_0ea72e23_fk_Comanda_id` (`comanda_id`),
  KEY `Detalle_producto_id_e4ace915_fk_Producto_id` (`producto_id`),
  KEY `Detalle_usuario_id_8cd91e0d_fk_Usuario_id` (`usuario_id`),
  KEY `Detalle_usuario_cancela_id_f7decb35_fk_Usuario_id` (`usuario_cancela_id`),
  KEY `Detalle_usuario_cobra_id_cf356a2a_fk_Usuario_id` (`usuario_cobra_id`),
  KEY `Detalle_usuario_elabora_id_ec143f1c_fk_Usuario_id` (`usuario_elabora_id`),
  KEY `Detalle_usuario_entrega_id_90d79baa_fk_Usuario_id` (`usuario_entrega_id`),
  KEY `Detalle_usuario_reasigna_id_a3579d0b_fk_Usuario_id` (`usuario_reasigna_id`),
  CONSTRAINT `Detalle_comanda_id_0ea72e23_fk_Comanda_id` FOREIGN KEY (`comanda_id`) REFERENCES `comanda` (`id`),
  CONSTRAINT `Detalle_producto_id_e4ace915_fk_Producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `Detalle_usuario_cancela_id_f7decb35_fk_Usuario_id` FOREIGN KEY (`usuario_cancela_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Detalle_usuario_cobra_id_cf356a2a_fk_Usuario_id` FOREIGN KEY (`usuario_cobra_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Detalle_usuario_elabora_id_ec143f1c_fk_Usuario_id` FOREIGN KEY (`usuario_elabora_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Detalle_usuario_entrega_id_90d79baa_fk_Usuario_id` FOREIGN KEY (`usuario_entrega_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Detalle_usuario_id_8cd91e0d_fk_Usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `Detalle_usuario_reasigna_id_a3579d0b_fk_Usuario_id` FOREIGN KEY (`usuario_reasigna_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle`
--

LOCK TABLES `detalle` WRITE;
/*!40000 ALTER TABLE `detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_Usuario_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_Usuario_id` FOREIGN KEY (`user_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-06-03 01:17:31.399650','1','evallardy',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'core','contable'),(7,'pedido','comanda'),(8,'pedido','detalle'),(11,'pedido','promocion'),(15,'producto','carne'),(14,'producto','cerveza'),(13,'producto','complemento'),(12,'producto','escarcha'),(19,'producto','grupo'),(9,'producto','producto'),(18,'producto','promocion'),(17,'producto','promociondetalle'),(16,'producto','sazona'),(5,'sessions','session'),(10,'usuario','usuario');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-05-28 23:19:09.272279'),(2,'contenttypes','0002_remove_content_type_name','2023-05-28 23:19:09.321135'),(3,'auth','0001_initial','2023-05-28 23:19:09.517699'),(4,'auth','0002_alter_permission_name_max_length','2023-05-28 23:19:09.565213'),(5,'auth','0003_alter_user_email_max_length','2023-05-28 23:19:09.573543'),(6,'auth','0004_alter_user_username_opts','2023-05-28 23:19:09.580792'),(7,'auth','0005_alter_user_last_login_null','2023-05-28 23:19:09.588045'),(8,'auth','0006_require_contenttypes_0002','2023-05-28 23:19:09.593479'),(9,'auth','0007_alter_validators_add_error_messages','2023-05-28 23:19:09.602394'),(10,'auth','0008_alter_user_username_max_length','2023-05-28 23:19:09.608773'),(11,'auth','0009_alter_user_last_name_max_length','2023-05-28 23:19:09.615356'),(12,'auth','0010_alter_group_name_max_length','2023-05-28 23:19:09.632550'),(13,'auth','0011_update_proxy_permissions','2023-05-28 23:19:09.642422'),(14,'auth','0012_alter_user_first_name_max_length','2023-05-28 23:19:09.650297'),(15,'usuario','0001_initial','2023-05-28 23:19:09.871284'),(16,'admin','0001_initial','2023-05-28 23:19:09.971596'),(17,'admin','0002_logentry_remove_auto_add','2023-05-28 23:19:09.980826'),(18,'admin','0003_logentry_add_action_flag_choices','2023-05-28 23:19:09.990794'),(19,'core','0001_initial','2023-05-28 23:19:10.009910'),(20,'core','0002_initial','2023-05-28 23:19:10.098183'),(21,'producto','0001_initial','2023-05-28 23:19:10.122284'),(22,'pedido','0001_initial','2023-05-28 23:19:10.235127'),(23,'pedido','0002_initial','2023-05-28 23:19:10.716839'),(24,'sessions','0001_initial','2023-05-28 23:19:10.750376'),(25,'core','0003_alter_contable_options','2023-06-01 12:39:52.106118'),(26,'usuario','0002_alter_usuario_options','2023-06-01 12:43:13.845060'),(27,'usuario','0003_usuario_celular','2023-06-01 17:44:03.099519'),(28,'core','0004_alter_contable_options','2023-06-02 16:50:35.722317'),(29,'core','0005_alter_contable_options','2023-06-02 21:37:48.476101'),(30,'usuario','0004_usuario_cliente','2023-06-03 16:50:27.983934'),(31,'usuario','0005_alter_usuario_cliente','2023-06-03 16:53:02.798411'),(32,'pedido','0003_comanda_usuario_cliente','2023-06-03 17:12:43.484569'),(33,'pedido','0004_alter_comanda_mesa','2023-06-05 10:03:59.179091'),(34,'producto','0002_producto_breve','2023-06-07 17:08:08.793873'),(35,'producto','0003_producto_promocion','2023-06-07 20:08:41.055791'),(36,'pedido','0005_detalle_varios_promocion','2023-06-08 20:26:59.244475'),(37,'producto','0004_remove_producto_promocion','2023-06-08 20:26:59.272925'),(38,'pedido','0006_remove_detalle_varios','2023-06-08 20:29:54.835841'),(39,'producto','0005_escarcha_complemento_cerveza','2023-06-10 12:25:16.833333'),(40,'producto','0006_producto_cerveza_producto_complemento_and_more','2023-06-10 12:27:53.199226'),(41,'producto','0007_alter_producto_tipo_carne','2023-06-10 15:37:21.298737'),(42,'producto','0008_producto_carne','2023-06-10 15:43:04.775625'),(43,'producto','0009_producto_sazonadores','2023-06-12 11:57:30.353149'),(44,'producto','0010_sazona','2023-06-12 12:12:21.501606'),(45,'producto','0011_rename_sazonadores_producto_sazonador','2023-06-12 12:17:04.459010'),(46,'producto','0012_carne_estatus_cerveza_estatus_complemento_estatus_and_more','2023-06-12 13:59:12.253948'),(47,'pedido','0007_delete_promocion','2023-06-12 20:27:56.784811'),(48,'producto','0013_promocion_promociondetalle','2023-06-12 20:27:56.914676'),(49,'producto','0014_promocion_tipo','2023-06-13 00:22:23.310084'),(50,'producto','0015_producto_drink','2023-06-13 23:19:37.243245'),(51,'producto','0016_producto_complemento_drink_producto_complemento_pan_and_more','2023-06-14 17:33:41.815483'),(52,'producto','0017_alter_producto_complemento_and_more','2023-06-14 17:39:35.600757'),(53,'producto','0018_delete_carne_delete_cerveza_delete_escarcha_and_more','2023-06-14 18:17:59.228521'),(54,'producto','0019_complemento_tipo','2023-06-16 23:15:10.048851'),(55,'producto','0020_alter_complemento_options_and_more','2023-06-16 23:53:09.136870'),(56,'producto','0021_alter_complemento_options','2023-06-22 23:31:18.833096'),(57,'producto','0022_alter_complemento_options','2023-06-22 23:41:35.508881'),(58,'producto','0023_alter_complemento_options','2023-06-23 01:20:23.153886'),(59,'producto','0024_alter_complemento_options','2023-06-23 01:44:55.144305'),(60,'producto','0025_alter_complemento_options','2023-06-23 01:59:44.026964'),(61,'producto','0026_rename_complemento_producto_complemento_cerveza','2023-06-24 15:36:44.874665'),(62,'pedido','0008_alter_comanda_estatus','2023-07-14 02:33:49.717570'),(63,'producto','0027_alter_promocion_tipo','2023-07-14 02:33:49.736281'),(64,'producto','0028_alter_promocion_options_grupo','2023-08-29 23:21:17.573992');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0m52qwu4nhvclvp919u8yrs1hp2vlhfl','.eJxVjEEOwiAQRe_C2pAZcCp16b5nIAMMUjU0Ke3KeHdD0oVu_uK_l_dWnvet-L3J6uekrsqp0-8XOD6ldpAeXO-Ljkvd1jnoruiDNj0tSV63w_0LFG6lZyUTIUeTMfRBO3LImA2cIcllFHCRB0CyNAAxBmMIbJbgHLnsrPp8Ae1-N5Q:1q6LAz:NjUnRm-z5pw5_7dTfHw5KaptOhFsqtJLTtEspiWHkBg','2023-06-19 19:07:57.070430'),('1gd7eyo4p4l5ady66r919ipb2i5eknaj','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1qCYKs:l2OLXOhluTSq-hIfktEnKn-dZE62s2nimGNejUDjGxo','2023-07-06 22:23:50.793933'),('5y8grt1t5jbol3391laalwu2hgavsghv','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1q8pFb:3KOc1mcPLn9rB5qAaoWfUNBAGXZbuGE0zV4uMw3tziw','2023-06-26 15:38:59.667988'),('eluf5v11ffjmjc1qbvfcca54j263wh8t','.eJxVjMsOwiAQRf-FtSGAPIpL9_0GMsNMpWpoUtqV8d-VpAvdnnPufYkE-1bS3nhNM4mLMOL0yxDyg2sXdId6W2Re6rbOKHsiD9vkuBA_r0f7d1Cgle8aOILykK3yTpngcrQ603R2WuMULZEewCFTMB0pzeQxKHDa-4ADZvH-AN9LN7k:1q5LcF:wVRskhmgiRgnlVlSV4tGV5uvZsVHpcCwPSk5GCGqIPY','2023-06-17 01:23:59.595523'),('es8scdcjwiw8dmx0gmobw9oo4ykvn74w','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1qa8B0:ijqBxNl1h3HJ7SUwMG7LhwJbPm7N0gw4qwfyChwaJZ0','2023-09-09 23:19:06.156111'),('ezxxhw3741o6tode4gecz6l9batf53pm','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1qHt1F:NJ50_57steuDGDWicHce23W8ov85dBRaMT_SgoJj3Ak','2023-07-21 15:29:37.217923'),('g87s4182pycafs3zpfli112g23fwaxb7','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1qFpSl:LhlUESOOIF1qgXddH3pzHdZa5ht1rbYK9tN6HjTQeiA','2023-07-15 23:17:31.103111'),('gqzrhpeas5xi2gqy4wgv04sndhsqipny','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1qNo1v:x-LZ7ujMGOsql-OeGU6D864uqAl5LyV1ryWHkQzWeE4','2023-08-06 23:22:47.295822'),('luoaorakd8l2jjpca7k2bpu7qy2j3urc','.eJxVjMsOwiAQRf-FtSFDhyng0r3fQBgeUjU0Ke3K-O_apAvd3nPOfQkftrX6refFT0mchRWn341DfOS2g3QP7TbLOLd1mVjuijxol9c55eflcP8Oauj1WyMAI1gySBAd4ZBAodMhwoiRAfKgyagUDSFbnbVjMxakwtqZoIsS7w-mkDao:1q6KoE:oeQF0ocyRtweX2s_ex1znq7xy0lRiKy-78wDxc4UOoY','2023-06-19 18:44:26.213340'),('mf1vw1gvekf20bomntb8p2stzd55n0sm','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1qKCxp:2cPKQblsa0H5J0YteKSvHaLyRQ17keKHBSHOorwRR7A','2023-07-28 01:11:41.848385'),('n4wxhpq6tmsdzen1lq8aoupjhr5m121i','.eJxVjDsOwyAQBe9CHSHAfFOm9xnQ4l2CkwgkY1dR7h5bcpG0b2bem0XY1hK3TkuckV2ZZJffLcH0pHoAfEC9Nz61ui5z4ofCT9r52JBet9P9OyjQy14bC6g1WZWBnFCQMbiUrMh-yFKK4FGG7EFh0nnaJYvOWDMYFMopQZZ9vvXDOAQ:1q5Dkl:qEVpqQUzX_5BbUzh0QcRJXIY_y4lSOzDw2mEn__Lyy4','2023-06-16 17:00:15.808597');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fechaoperacion`
--

DROP TABLE IF EXISTS `fechaoperacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fechaoperacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `observacion` varchar(255) DEFAULT NULL,
  `estatus` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `usuario_abre_id` bigint DEFAULT NULL,
  `usuario_cierra_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FechaOperacion_usuario_abre_id_69c9f6c2_fk_Usuario_id` (`usuario_abre_id`),
  KEY `FechaOperacion_usuario_cierra_id_7ebeddd4_fk_Usuario_id` (`usuario_cierra_id`),
  CONSTRAINT `FechaOperacion_usuario_abre_id_69c9f6c2_fk_Usuario_id` FOREIGN KEY (`usuario_abre_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `FechaOperacion_usuario_cierra_id_7ebeddd4_fk_Usuario_id` FOREIGN KEY (`usuario_cierra_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fechaoperacion`
--

LOCK TABLES `fechaoperacion` WRITE;
/*!40000 ALTER TABLE `fechaoperacion` DISABLE KEYS */;
INSERT INTO `fechaoperacion` VALUES (12,'2023-06-07',NULL,1,'2023-06-07 23:15:03.749870','2023-06-07 23:15:03.749870',1,NULL);
/*!40000 ALTER TABLE `fechaoperacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupo`
--

DROP TABLE IF EXISTS `grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grupo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `estatus` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Grupo_nombre_4b2f5a54_uniq` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupo`
--

LOCK TABLES `grupo` WRITE;
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `tipo` int NOT NULL,
  `ingredientes` json DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `estatus` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `breve` varchar(255) DEFAULT NULL,
  `cerveza` int NOT NULL,
  `complemento_cerveza` int NOT NULL,
  `escarcha` int NOT NULL,
  `carne` int NOT NULL,
  `sazonador` int NOT NULL,
  `drink` int NOT NULL,
  `complemento_drink` int NOT NULL,
  `complemento_pan` int NOT NULL,
  `complemento_wing` int NOT NULL,
  `refresco` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (45,'CERVEZA',2,'\"\"',70.00,1,'2023-06-25 03:38:44.551300','2023-06-14 18:35:44.119203',NULL,1,0,0,0,0,0,0,0,0,0),(47,'JOCHOS',1,'[\"Aderezo\", \"Cebolla\", \"Jalapeño\", \"Jitomate\", \"Tocino\"]',50.00,1,'2023-06-25 03:21:01.621427','2023-06-14 18:38:11.075165','Dos piezas (aderezo, jitomate, cebolla, jalapeño y tocino',0,0,0,0,0,0,0,1,0,0),(48,'BURGERS',1,'\"\"',65.00,1,'2023-06-25 03:22:17.641220','2023-06-14 18:39:15.544888',NULL,0,0,0,1,0,0,0,1,0,0),(49,'STORMTROOPERS',2,'\"\"',80.00,1,'2023-06-25 03:38:05.190999','2023-06-17 16:58:35.508045','Tu cerveza preparada',1,1,1,0,0,0,0,0,0,0),(50,'WiNGS BBQ',1,'[\"Receta de la casa\"]',65.00,1,'2023-06-25 02:49:11.402940','2023-06-17 17:01:58.560580','Dulces y sabrositas con la receta de la casa.',0,0,0,0,0,0,0,0,1,0),(51,'PAPAS A LA FRANCESA',1,'\"\"',45.00,1,'2023-06-25 03:38:22.884065','2023-06-24 18:52:03.970401','Elije tu sazonador',0,0,0,0,1,0,0,0,0,0),(52,'BURGERS + papas',1,'\"\"',85.00,1,'2023-06-25 03:39:03.864064','2023-06-24 19:41:35.495730','Res o Pollo',0,0,0,1,0,0,0,1,0,0),(58,'DARTH MAUL',2,'[\"Licor de frutos rojos\", \"Toque especial\", \"Vodka\", \"Soda\"]',70.00,1,'2023-06-25 02:35:38.813327','2023-06-24 20:03:07.577901','Bebida con licor de frutos rojos, soda y nuestro toque especial.',0,0,0,0,0,1,1,0,0,1),(59,'JEDI',2,'[\"Curacao azul\", \"Toque especial\", \"Vodka\", \"Soda\"]',70.00,1,'2023-06-25 02:34:45.152284','2023-06-24 22:23:12.674593','Bebida con curacao azul, soda y nuestro toque especial',0,0,0,0,0,1,1,0,0,1),(60,'C3PO',2,'[\"Licor de mango piña\", \"Vodka\", \"Soda\"]',70.00,1,'2023-06-25 02:36:14.797457','2023-06-24 22:27:40.742687','Bebida con licor de explosivo mango - piña y soda.',0,0,0,0,0,1,1,0,0,1),(61,'BABY YODA',2,'[\"Licor de manzana verde\", \"Menta\", \"Vodka\", \"Soda\"]',70.00,1,'2023-06-25 02:36:58.879617','2023-06-24 22:29:00.620167','Bebida con licor cósmico de manzana verde, toque de menta fresca y soda.',0,0,0,0,0,1,1,0,0,1),(62,'DARTH VADER',2,'[\"Licor de uva\", \"Toque especial\", \"Vodka\", \"Soda\"]',70.00,1,'2023-06-25 02:37:44.455086','2023-06-24 22:30:13.528010','Bebida con licor de uva galáctica, soda y nuestro toque especial.',0,0,0,0,0,1,1,0,0,1),(63,'LUKE SKY- WALKER',2,'[\"Receta especial\", \"Sky vodka\"]',90.00,1,'2023-06-25 02:39:19.995729','2023-06-24 22:31:06.140775','Sky vodka preparado con la receta especial.',0,0,0,0,0,1,1,0,0,1),(64,'MANDALORIANO',2,'[\"Agua mineral\", \"Menta\", \"Sabor cítrico\", \"Ron\"]',70.00,1,'2023-06-25 02:40:27.647511','2023-06-24 22:33:36.344609','El cubano mojito con sabor cítrico, menta y agua mineral.',0,0,0,0,0,1,1,0,0,1),(65,'R2D2',2,'[\"Crema de coco\", \"Jugo de piña\", \"Ron\"]',70.00,1,'2023-06-25 02:40:56.261017','2023-06-24 22:34:42.893877','Cremosa y refrescante piña y crema de coco.',0,0,0,0,0,1,1,0,0,1),(66,'PRINCESA LEIA',2,'[\"Crema de coco\", \"Jugo de piña colada\", \"Toque de rosas\", \"Ron\"]',70.00,1,'2023-06-25 02:42:19.134845','2023-06-24 22:35:45.071231','Dulce jugo de piña colada con crema de coco y un toque de rosas.',0,0,0,0,0,1,1,0,0,1),(67,'CHEWBACCA',2,'[\"Licor de café\", \"Receta especial\", \"Brandy\"]',70.00,1,'2023-06-25 02:42:55.599261','2023-06-24 22:36:46.836876','A base de brandy, licor de café con la receta especial.',0,0,0,0,0,1,1,0,0,1),(68,'JABBA',2,'[\"Picosito\", \"Sabor cítrico\", \"Tequila\"]',70.00,1,'2023-06-25 02:44:12.001414','2023-06-24 22:38:41.076495','Sabor cítrico, tradicional y picosito',0,0,0,0,0,1,1,0,0,1),(69,'EWOK',2,'[\"Agua mineral\", \"Menta\", \"Sabor cítrico\", \"Tequila\"]',70.00,1,'2023-06-25 02:44:31.382934','2023-06-24 22:39:27.945047','Refrescante sabor cítrico, menta y agua mineral.',0,0,0,0,0,1,1,0,0,1),(71,'CLON 001',2,'[\"Gin\", \"Menta\", \"Pepino\", \"Sabor cítrico\", \"Vodka\"]',50.00,1,'2023-06-24 22:41:16.210400','2023-06-24 22:41:16.210400','Vodka & gin, sabor cítrico , pepino y un toque de menta.',0,0,0,0,0,1,1,0,0,1),(72,'CLON 002',2,'[\"Crema de coco\", \"Curacao azul\", \"Jugo de piña\", \"Ron\"]',50.00,1,'2023-06-24 22:42:26.575618','2023-06-24 22:42:26.575618','Blue Hawaian elaborado a base de ron, jugo de piña, curacao azul y crema de coco.',0,0,0,0,0,1,1,0,0,1),(73,'CLON 003',2,'[\"Jugo de naranja\", \"Toque especial\", \"Vodka\"]',50.00,1,'2023-06-24 22:43:31.806945','2023-06-24 22:43:31.806945','Desarmador clásica, bebida preparada a base de vodka y jugo de naranja con un toque especial.',0,0,0,0,0,1,1,0,0,1),(74,'CLON 004',2,'[\"Jugo de toronja\", \"Menta\", \"Tequila\", \"Soda\"]',50.00,1,'2023-06-24 22:44:40.253607','2023-06-24 22:44:40.253607','Paloma tradicional y refrescante preparada a base de tequila y jugo de toronja, con un toque especial de menta fresca y soda.',0,0,0,0,0,1,1,0,0,1),(75,'CLON 005',2,'[\"Jugo de limón\", \"Ron\", \"Coca Cola\"]',50.00,1,'2023-06-25 02:48:38.004799','2023-06-24 22:45:38.096363','Clásica y refrescante cuba libre con refresco de cola y jugo de limón.',0,0,0,0,0,1,1,0,0,1),(76,'EMPERADOR',2,'[\"Curacao azul\", \"Toque de la casa\", \"Tequila\"]',70.00,1,'2023-06-25 02:45:58.184234','2023-06-25 02:45:58.184234','Bebida a base de tequila, curacao azul y el toque de la casa.',0,0,0,0,0,1,1,0,0,1),(77,'WINGS FRUTOS ROJOS',1,'[\"Mezcal\", \"Salsita de fresa blueberry\"]',65.00,1,'2023-06-25 03:09:12.639474','2023-06-25 02:51:32.479737','Picosita salsita de fresa-blueberry con mezcal.',0,0,0,0,0,0,0,0,1,0),(78,'WINGS MANGO HABANERO',1,'[\"Mezcal\", \"Salsita de mango-piña\"]',65.00,1,'2023-06-25 03:10:28.498469','2023-06-25 03:10:28.498469','Picosita salsita de mango-piña con mezcal',0,0,0,0,0,0,0,0,1,0),(79,'WiNGS BBQ + papas',1,'[\"Receta de la casa\"]',90.00,1,'2023-06-25 03:39:15.615320','2023-06-25 03:15:51.050099','Dulces y sabrositas con la receta de la casa.',0,0,0,0,0,0,0,0,1,0),(80,'WINGS FRUTOS ROJOS + papas',1,'[\"Mezcal\", \"Salsita de fresa blueberry\"]',90.00,1,'2023-06-25 03:39:23.900417','2023-06-25 03:17:35.662254',NULL,0,0,0,0,0,0,0,0,1,0),(81,'WINGS MANGO HABANERO + papas',1,'\"\"',90.00,1,'2023-06-25 03:39:33.298642','2023-06-25 03:18:35.461883','Picosita salsita de mango-piña con mezcal',0,0,0,0,0,0,0,0,0,0),(82,'JOCHOS + papas',1,'[\"Aderezo\", \"Cebolla\", \"Jalapeño\", \"Jitomate\", \"Tocino\"]',75.00,1,'2023-06-25 03:39:09.183084','2023-06-25 03:20:40.975449','Dos piezas (aderezo, jitomate, cebolla, jalapeño y tocino.',0,0,0,0,0,0,0,1,0,0),(83,'DRINK',2,'\"\"',70.00,1,'2023-06-26 01:44:56.796475','2023-06-26 01:44:56.796475',NULL,0,0,0,0,0,1,1,0,0,1),(84,'WINGS',1,'\"\"',55.00,1,'2023-06-26 01:49:13.209930','2023-06-26 01:49:13.209930','Alitas al natural',0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promocion`
--

DROP TABLE IF EXISTS `promocion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promocion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `estatus` int NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `tipo` int NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promocion`
--

LOCK TABLES `promocion` WRITE;
/*!40000 ALTER TABLE `promocion` DISABLE KEYS */;
INSERT INTO `promocion` VALUES (15,'CORELIA',1,220.00,'2023-07-24 01:56:01.198186','2023-06-25 22:42:12.547003',2,NULL),(16,'DRINK´S AL PAR',1,120.00,'2023-06-26 01:45:59.268656','2023-06-26 01:45:59.253391',2,NULL),(17,'CAZA ESTELAR WINGS',1,250.00,'2023-07-24 01:55:21.539568','2023-06-26 01:50:38.224157',1,'Dos stormtroopers, una orden de wings con papas\r\ngrandes'),(18,'CAZA ESTELAR BURGER',1,310.00,'2023-07-24 01:55:16.073087','2023-06-26 01:56:18.612099',1,'Dos stormtroopers, dos burgers con papas grandes'),(19,'CAZA ESTELAR AMIGO',1,270.00,'2023-07-24 01:55:09.109272','2023-06-26 01:58:59.945199',1,'Dos drinks, dos burgers con papas grandes.'),(20,'DESTRUCTOR ESTELAR STORMTROOPERS',1,375.00,'2023-07-24 01:55:33.063805','2023-06-26 02:01:15.558719',1,'Tres stormtroopers, dos ordenes de wings con papas grandes.'),(21,'DESTRUCTOR ESTELAR DRINKS',1,390.00,'2023-07-24 01:55:27.223147','2023-06-26 02:03:15.288901',1,'Cuatro drinks, dos ordenes de wings con papas grandes.'),(22,'HALCON MILENARIO STORMTROOPERS',1,825.00,'2023-07-24 01:55:46.261227','2023-06-26 02:05:55.324109',1,'Seis stormtroopers, dos ordenes de wings, dos ordenes de Jochos y dos hamburguesas con papas grandes.'),(23,'HALCON MILENARIO DRINK\'S',1,745.00,'2023-07-24 01:55:40.641800','2023-06-26 02:07:36.534075',1,'Seis drinks, dos ordenes de wings, dos Jochos y dos hamburguesas con papas grandes.');
/*!40000 ALTER TABLE `promocion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promociondetalle`
--

DROP TABLE IF EXISTS `promociondetalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promociondetalle` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `producto_id` bigint NOT NULL,
  `promocion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `PromocionDetalle_producto_id_b5b9c083_fk_Producto_id` (`producto_id`),
  KEY `PromocionDetalle_promocion_id_6fa92818_fk_Promocion_id` (`promocion_id`),
  CONSTRAINT `PromocionDetalle_producto_id_b5b9c083_fk_Producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`id`),
  CONSTRAINT `PromocionDetalle_promocion_id_6fa92818_fk_Promocion_id` FOREIGN KEY (`promocion_id`) REFERENCES `promocion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promociondetalle`
--

LOCK TABLES `promociondetalle` WRITE;
/*!40000 ALTER TABLE `promociondetalle` DISABLE KEYS */;
INSERT INTO `promociondetalle` VALUES (85,3,'2023-07-24 01:56:01.194802','2023-06-26 00:50:44.338341',49,15),(91,2,'2023-06-26 01:45:59.265652','2023-06-26 01:45:59.265652',83,16),(92,1,'2023-07-24 01:55:21.533604','2023-06-26 01:50:38.225157',84,17),(93,2,'2023-07-24 01:55:21.535976','2023-06-26 01:50:38.226230',49,17),(94,1,'2023-07-24 01:55:21.530642','2023-06-26 01:54:55.987545',51,17),(95,2,'2023-07-24 01:55:16.067216','2023-06-26 01:56:18.613837',52,18),(96,2,'2023-07-24 01:55:16.069857','2023-06-26 01:56:18.614916',49,18),(97,2,'2023-07-24 01:55:09.101843','2023-06-26 01:58:59.946198',52,19),(98,3,'2023-07-24 01:55:33.059620','2023-06-26 02:01:15.560719',49,20),(99,1,'2023-07-24 01:55:33.054514','2023-06-26 02:01:55.025425',51,20),(100,2,'2023-07-24 01:55:33.056507','2023-06-26 02:01:55.025425',84,20),(101,4,'2023-07-24 01:55:27.218382','2023-06-26 02:03:15.290905',83,21),(102,2,'2023-07-24 01:55:27.213482','2023-06-26 02:03:15.290905',51,21),(103,2,'2023-07-24 01:55:27.215475','2023-06-26 02:03:15.292409',84,21),(104,6,'2023-07-24 01:55:46.257017','2023-06-26 02:05:55.336117',49,22),(105,2,'2023-07-24 01:55:46.253917','2023-06-26 02:05:55.337118',84,22),(106,2,'2023-07-24 01:55:46.249203','2023-06-26 02:05:55.338337',82,22),(107,2,'2023-07-24 01:55:46.246632','2023-06-26 02:05:55.339342',52,22),(108,2,'2023-07-24 01:55:46.251618','2023-06-26 02:05:55.339342',51,22),(109,6,'2023-07-24 01:55:40.637711','2023-06-26 02:07:36.545886',83,23),(110,2,'2023-07-24 01:55:40.635174','2023-06-26 02:07:36.546920',84,23),(111,2,'2023-07-24 01:55:40.629797','2023-06-26 02:07:36.547948',82,23),(112,2,'2023-07-24 01:55:40.627234','2023-06-26 02:07:36.548888',52,23),(113,2,'2023-07-24 01:55:40.631809','2023-06-26 02:07:36.550140',51,23),(114,2,'2023-07-24 01:55:09.104312','2023-07-01 23:29:26.167836',83,19);
/*!40000 ALTER TABLE `promociondetalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `celular` varchar(20) DEFAULT NULL,
  `cliente` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'pbkdf2_sha256$320000$SxNwOqbtBLsTAJCMZIBOiP$6sd1AW+jaVUtizfIIwKvQ9NKoavKoC1xFJ5FXsYz8hY=','2023-08-26 23:19:06.150635',1,'evallardy','Enrique','Vallardy Montes de Oca','evallardy@gmail.com',1,1,'2023-05-28 23:22:50.000000','551580',0),(2,'pbkdf2_sha256$320000$DhBbtXB4G69RJ4eHbn0Vkz$/9Oz0Q+GoaMTwTlCv+LcAsAwew2Omt98snfVoXHR2UQ=','2023-06-03 01:23:59.593539',0,'jcamarillo','Javier','Camarillo','camarillo.javier@gmail.com',0,1,'2023-06-02 01:20:26.646992','2312312',0),(3,'pbkdf2_sha256$320000$roqIOfwIY6Z0CsCKTAwp7m$ISBPmOmH+ZrFRCgRMqOtc5MJU2e3EZOfkYma2F8IEqA=',NULL,0,'gtroncoso','Gerardo','Troncoso','',0,1,'2023-06-02 01:22:00.212922','123123',0),(4,'pbkdf2_sha256$320000$niWZJpnSxAW39vQ6KKimSH$eGKOYdNFtrnWryhgpdW3nrbm4jEIbSt2GBiyEmPAGr8=',NULL,0,'dvallardy','Daniel','Vallardy','dani@ggg.com',0,1,'2023-06-02 01:24:26.137350','3123123',0),(5,'pbkdf2_sha256$320000$WK6MOiAtN3XyOuHAH2tKRS$DS5q3FHhwRzs8Jejtp/sVjwVtVlc9WqQLfqr3NU20VM=',NULL,0,'trenzador','Tere','Velazquez','asdad@adasd.com',0,1,'2023-06-02 01:57:22.404769','123123',0),(8,'pbkdf2_sha256$320000$3AUSiSwi1m0Uis4qlL0uRB$Rwchy1o4er+RRgdIdmYJ8LKjumkqG9wfUy3QXcA9qpI=','2023-06-07 23:14:31.698338',0,'rtamiz','Roberto','Tamiz Hernandez','aeeee@sssss.com',0,1,'2023-06-03 19:02:26.486459','000000000',1);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_groups`
--

DROP TABLE IF EXISTS `usuario_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Usuario_groups_usuario_id_group_id_066ea720_uniq` (`usuario_id`,`group_id`),
  KEY `Usuario_groups_group_id_41c3a916_fk_auth_group_id` (`group_id`),
  CONSTRAINT `Usuario_groups_group_id_41c3a916_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `Usuario_groups_usuario_id_48f41311_fk_Usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_groups`
--

LOCK TABLES `usuario_groups` WRITE;
/*!40000 ALTER TABLE `usuario_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_user_permissions`
--

DROP TABLE IF EXISTS `usuario_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `usuario_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Usuario_user_permissions_usuario_id_permission_id_214e1f37_uniq` (`usuario_id`,`permission_id`),
  KEY `Usuario_user_permiss_permission_id_614dc495_fk_auth_perm` (`permission_id`),
  CONSTRAINT `Usuario_user_permiss_permission_id_614dc495_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `Usuario_user_permissions_usuario_id_a4d95b6f_fk_Usuario_id` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_user_permissions`
--

LOCK TABLES `usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuario_user_permissions` DISABLE KEYS */;
INSERT INTO `usuario_user_permissions` VALUES (38,1,118),(29,2,101),(42,2,102),(41,2,103),(30,2,104),(43,2,105),(44,2,106),(59,2,107),(62,2,108),(64,2,109),(60,2,110),(63,2,111),(61,2,112),(65,2,113),(37,2,114),(46,2,115),(45,2,116),(35,2,117),(47,2,118),(48,2,119),(49,2,120),(50,2,121),(52,2,122),(56,2,123),(58,2,124),(67,2,125),(31,2,126),(36,2,127),(53,2,128),(54,2,129),(57,4,123);
/*!40000 ALTER TABLE `usuario_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-29 23:31:56
