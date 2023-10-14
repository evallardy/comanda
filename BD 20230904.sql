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
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add Fecha de operación',6,'add_contable'),(22,'Can change Fecha de operación',6,'change_contable'),(23,'Can delete Fecha de operación',6,'delete_contable'),(24,'Can view Fecha de operación',6,'view_contable'),(25,'Cocina consulta',6,'cocina'),(26,'Cocina termina',6,'cocina_termina'),(27,'Cocina cancela',6,'cocina_cancela'),(28,'Bar consulta',6,'bar'),(29,'Bar termina',6,'bar_termina'),(30,'Bar cancela',6,'bar_cancela'),(31,'Comandas consulta',6,'servicio'),(32,'Comanda nueva',6,'servicio_nueva'),(33,'Comanda solicita',6,'servicio_solicitar'),(34,'Comanda cancela',6,'servicio_cancelar'),(35,'Comanda paga',6,'servicio_pagar'),(36,'Comanda detalle',6,'servicio_ver'),(37,'Comanda cierra',6,'servicio_cierra'),(38,'Entregas consulta',6,'entregas'),(39,'Entrega OK',6,'entregas_ok'),(40,'Entrega cancelada',6,'entregas_cancela'),(41,'Reasignar',6,'reasignar'),(42,'Consulta de seguimiento',6,'consultas_seguimiento'),(43,'Consulta de reporte del día',6,'consultas_reporte_dia'),(44,'Catálogo consulta',6,'catalogo'),(45,'Catálogo Agrega',6,'catalogo_agregar'),(46,'Catáogo Modifica',6,'catalogo_modificar'),(47,'Accesos consulta',6,'accesos'),(48,'Accesos modifica',6,'accesos_modificar'),(49,'Día abre',6,'abrir'),(50,'Día cierra',6,'cerrar'),(51,'Usuarios consulta',6,'usuarios'),(52,'Usuario nuevo',6,'crea_usuario'),(53,'Usuario modifica',6,'modifica_usuario'),(54,'Can add Comanda',7,'add_comanda'),(55,'Can change Comanda',7,'change_comanda'),(56,'Can delete Comanda',7,'delete_comanda'),(57,'Can view Comanda',7,'view_comanda'),(58,'Can add Detalle',8,'add_detalle'),(59,'Can change Detalle',8,'change_detalle'),(60,'Can delete Detalle',8,'delete_detalle'),(61,'Can view Detalle',8,'view_detalle'),(62,'Can add Grupo',9,'add_grupo'),(63,'Can change Grupo',9,'change_grupo'),(64,'Can delete Grupo',9,'delete_grupo'),(65,'Can view Grupo',9,'view_grupo'),(66,'Can add Promocion',10,'add_paquete'),(67,'Can change Promocion',10,'change_paquete'),(68,'Can delete Promocion',10,'delete_paquete'),(69,'Can view Promocion',10,'view_paquete'),(70,'Can add Producto',11,'add_producto'),(71,'Can change Producto',11,'change_producto'),(72,'Can delete Producto',11,'delete_producto'),(73,'Can view Producto',11,'view_producto'),(74,'Can add Complemento',12,'add_insumo'),(75,'Can change Complemento',12,'change_insumo'),(76,'Can delete Complemento',12,'delete_insumo'),(77,'Can view Complemento',12,'view_insumo'),(78,'Can add usuario',13,'add_usuario'),(79,'Can change usuario',13,'change_usuario'),(80,'Can delete usuario',13,'delete_usuario'),(81,'Can view usuario',13,'view_usuario');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comanda`
--

LOCK TABLES `comanda` WRITE;
/*!40000 ALTER TABLE `comanda` DISABLE KEYS */;
/*!40000 ALTER TABLE `comanda` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(6,'core','contable'),(7,'pedido','comanda'),(8,'pedido','detalle'),(9,'producto','grupo'),(12,'producto','insumo'),(10,'producto','paquete'),(11,'producto','producto'),(5,'sessions','session'),(13,'usuario','usuario');
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-08-30 00:51:39.325500'),(2,'contenttypes','0002_remove_content_type_name','2023-08-30 00:51:39.373740'),(3,'auth','0001_initial','2023-08-30 00:51:39.547443'),(4,'auth','0002_alter_permission_name_max_length','2023-08-30 00:51:39.600250'),(5,'auth','0003_alter_user_email_max_length','2023-08-30 00:51:39.607815'),(6,'auth','0004_alter_user_username_opts','2023-08-30 00:51:39.613039'),(7,'auth','0005_alter_user_last_login_null','2023-08-30 00:51:39.621590'),(8,'auth','0006_require_contenttypes_0002','2023-08-30 00:51:39.627211'),(9,'auth','0007_alter_validators_add_error_messages','2023-08-30 00:51:39.635427'),(10,'auth','0008_alter_user_username_max_length','2023-08-30 00:51:39.646056'),(11,'auth','0009_alter_user_last_name_max_length','2023-08-30 00:51:39.653553'),(12,'auth','0010_alter_group_name_max_length','2023-08-30 00:51:39.671878'),(13,'auth','0011_update_proxy_permissions','2023-08-30 00:51:39.679205'),(14,'auth','0012_alter_user_first_name_max_length','2023-08-30 00:51:39.687334'),(15,'usuario','0001_initial','2023-08-30 00:51:39.870039'),(16,'admin','0001_initial','2023-08-30 00:51:39.962951'),(17,'admin','0002_logentry_remove_auto_add','2023-08-30 00:51:39.972224'),(18,'admin','0003_logentry_add_action_flag_choices','2023-08-30 00:51:39.979282'),(19,'core','0001_initial','2023-08-30 00:51:40.002906'),(20,'core','0002_initial','2023-08-30 00:51:40.099626'),(21,'producto','0001_initial','2023-08-30 00:51:40.225731'),(22,'pedido','0001_initial','2023-08-30 00:51:40.325635'),(23,'pedido','0002_initial','2023-08-30 00:51:40.804198'),(24,'sessions','0001_initial','2023-08-30 00:51:40.838557'),(25,'producto','0002_alter_insumo_options_alter_paquete_options_and_more','2023-08-30 01:20:49.352841'),(26,'producto','0003_alter_insumo_options_alter_insumo_unique_together_and_more','2023-08-30 01:43:48.694340'),(27,'producto','0004_alter_insumo_unique_together','2023-08-31 22:41:46.849960'),(28,'producto','0005_remove_producto_preparado','2023-09-02 02:56:29.705235'),(29,'producto','0006_rename_ingredientes_producto_insumos','2023-09-02 02:57:15.763061'),(30,'producto','0007_insumo_imagen_paquete_imagen_producto_imagen','2023-09-04 20:20:53.146210');
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
INSERT INTO `django_session` VALUES ('t04t5snudd2h2kzjaavkn1kfpgsoslme','.eJxVjEEOwiAQAP_C2RCgu4V69N43kAUWWzWQlPZk_Lsh6UGvM5N5C0_Hvvij8ebXJK5Ci8svCxSfXLpIDyr3KmMt-7YG2RN52ibnmvh1O9u_wUJt6duAaJHdxArRqBECKMUmGxgsoSIYctBggcacbXQ5xckxkjEwDdoaKz5fuv824w:1qbGCp:cavd07-Wof8AenusjfB77agK_vHWP_reHWRi3xXRC8s','2023-09-13 02:05:39.199716');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fechaoperacion`
--

LOCK TABLES `fechaoperacion` WRITE;
/*!40000 ALTER TABLE `fechaoperacion` DISABLE KEYS */;
INSERT INTO `fechaoperacion` VALUES (1,'2023-08-30',NULL,1,'2023-08-30 00:54:02.062828','2023-08-30 00:54:02.062828',1,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupo`
--

LOCK TABLES `grupo` WRITE;
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` VALUES (1,'Cerveza',1,'2023-08-30 02:54:32.916835','2023-08-30 02:54:32.916835'),(2,'Complementos de cerveza',1,'2023-08-30 03:10:05.795435','2023-08-30 03:10:05.795435'),(3,'Carnes',1,'2023-08-30 23:57:41.780452','2023-08-30 23:57:41.780452'),(4,'Vegetales',1,'2023-08-30 23:57:52.082628','2023-08-30 23:57:52.082628'),(5,'Complemento drink',1,'2023-08-30 23:58:07.652294','2023-08-30 23:58:07.652294'),(6,'Lácteos',1,'2023-08-30 23:59:48.176086','2023-08-30 23:59:48.176086'),(7,'Complemento Alitas',1,'2023-08-31 00:00:01.545794','2023-08-31 00:00:01.545794'),(8,'Bebidas',1,'2023-08-31 00:04:30.656447','2023-08-31 00:00:11.778452'),(9,'Escarcha',1,'2023-08-31 00:00:19.103902','2023-08-31 00:00:19.103902'),(10,'Refresco',1,'2023-08-31 00:00:28.573098','2023-08-31 00:00:28.573098'),(11,'Sazonador',1,'2023-08-31 00:00:38.173266','2023-08-31 00:00:38.173266'),(12,'Complemento comida',1,'2023-08-31 22:50:55.834461','2023-08-31 22:50:55.834461');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insumo`
--

DROP TABLE IF EXISTS `insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insumo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `estatus` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `grupo_id` bigint NOT NULL,
  `imagen` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Insumo_grupo_id_nombre_7fd41859_uniq` (`grupo_id`,`nombre`),
  CONSTRAINT `Complemento_grupo_id_156432f2_fk_Grupo_id` FOREIGN KEY (`grupo_id`) REFERENCES `grupo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insumo`
--

LOCK TABLES `insumo` WRITE;
/*!40000 ALTER TABLE `insumo` DISABLE KEYS */;
INSERT INTO `insumo` VALUES (1,'Res',1,'2023-08-31 01:07:01.354013','2023-08-31 01:07:01.354013',3,NULL),(2,'Pollo',1,'2023-08-31 01:09:29.212950','2023-08-31 01:09:29.212950',3,NULL),(3,'Salchicha',1,'2023-08-31 01:10:40.503015','2023-08-31 01:10:40.503015',3,NULL),(4,'Alitas',1,'2023-08-31 01:37:23.835155','2023-08-31 01:11:52.375932',3,NULL),(5,'Papas',1,'2023-08-31 01:33:31.333126','2023-08-31 01:33:31.333126',4,NULL),(6,'Brandy',1,'2023-08-31 22:34:53.984702','2023-08-31 22:34:53.984702',8,NULL),(8,'Ron',1,'2023-08-31 22:35:07.278999','2023-08-31 22:35:07.278999',8,NULL),(9,'Sky vodka',1,'2023-08-31 22:35:13.625149','2023-08-31 22:35:13.625149',8,NULL),(10,'Tequila',1,'2023-08-31 22:35:27.845455','2023-08-31 22:35:27.845455',8,NULL),(11,'Vodka',1,'2023-08-31 22:35:34.364149','2023-08-31 22:35:34.364149',8,NULL),(12,'Budweisser',1,'2023-08-31 22:39:08.245767','2023-08-31 22:39:08.245767',1,NULL),(13,'Corona',1,'2023-08-31 22:39:16.411343','2023-08-31 22:39:16.411343',1,NULL),(14,'Heineken',1,'2023-08-31 22:39:24.986501','2023-08-31 22:39:24.986501',1,NULL),(15,'Indio',1,'2023-08-31 22:39:31.693700','2023-08-31 22:39:31.694785',1,NULL),(16,'León',1,'2023-08-31 22:39:36.734900','2023-08-31 22:39:36.734900',1,NULL),(17,'Miller',1,'2023-08-31 22:39:43.258553','2023-08-31 22:39:43.258553',1,NULL),(18,'Modelo',1,'2023-08-31 22:39:52.354082','2023-08-31 22:39:52.354082',1,NULL),(19,'Negra modelo',1,'2023-08-31 22:39:58.387715','2023-08-31 22:39:58.387715',1,NULL),(20,'Victoria',1,'2023-08-31 22:40:04.785924','2023-08-31 22:40:04.785924',1,NULL),(21,'XX Ambar',1,'2023-08-31 22:40:10.971192','2023-08-31 22:40:10.971192',1,NULL),(22,'XX Lager',1,'2023-08-31 22:40:17.643480','2023-08-31 22:40:17.643480',1,NULL),(23,'Mezcal',1,'2023-08-31 22:41:57.853272','2023-08-31 22:41:57.853272',8,NULL),(24,'Salsita de mango-piña',1,'2023-08-31 22:42:29.704019','2023-08-31 22:42:06.949836',7,NULL),(25,'Receta de la casa',1,'2023-08-31 22:42:12.409086','2023-08-31 22:42:12.409086',7,NULL),(26,'Salsita de fresa blueberry',1,'2023-08-31 22:42:17.836000','2023-08-31 22:42:17.836000',7,NULL),(27,'Crema de coco',1,'2023-08-31 22:48:02.190486','2023-08-31 22:48:02.190486',5,NULL),(28,'Curacao azul',1,'2023-08-31 22:48:09.546682','2023-08-31 22:48:09.546682',5,NULL),(29,'Gin',1,'2023-08-31 22:48:15.482743','2023-08-31 22:48:15.482743',5,NULL),(30,'Jugo de limón',1,'2023-08-31 22:48:23.353821','2023-08-31 22:48:23.353821',5,NULL),(31,'Jugo de naranja',1,'2023-08-31 22:48:30.136886','2023-08-31 22:48:30.136886',5,NULL),(32,'Jugo de piña',1,'2023-08-31 22:48:37.024320','2023-08-31 22:48:37.024320',5,NULL),(33,'Jugo de piña colada',1,'2023-08-31 22:48:41.768195','2023-08-31 22:48:41.768195',5,NULL),(34,'Jugo de toronja',1,'2023-08-31 22:48:46.412696','2023-08-31 22:48:46.412696',5,NULL),(35,'Licor de café',1,'2023-08-31 22:48:51.819174','2023-08-31 22:48:51.819174',5,NULL),(36,'Licor de frutos rojos',1,'2023-08-31 22:48:56.738615','2023-08-31 22:48:56.738615',5,NULL),(37,'Licor de mango piña',1,'2023-08-31 22:49:00.875003','2023-08-31 22:49:00.875003',5,NULL),(38,'Licor de manzana verde',1,'2023-08-31 22:49:06.258712','2023-08-31 22:49:06.258712',5,NULL),(39,'Licor de uva',1,'2023-08-31 22:49:10.485398','2023-08-31 22:49:10.485398',5,NULL),(40,'Menta',1,'2023-08-31 22:49:15.148662','2023-08-31 22:49:15.148662',5,NULL),(41,'Pepino',1,'2023-08-31 22:49:21.710271','2023-08-31 22:49:21.710271',5,NULL),(42,'Picosito',1,'2023-08-31 22:49:30.309494','2023-08-31 22:49:30.309494',5,NULL),(43,'Receta especial',1,'2023-08-31 22:49:39.022044','2023-08-31 22:49:39.022044',5,NULL),(44,'Sabor cítrico',1,'2023-08-31 22:49:43.753825','2023-08-31 22:49:43.753825',5,NULL),(45,'Toque de la casa',1,'2023-08-31 22:49:48.124069','2023-08-31 22:49:48.124069',5,NULL),(46,'Toque de rosas',1,'2023-08-31 22:49:52.844580','2023-08-31 22:49:52.844580',5,NULL),(47,'Toque especial',1,'2023-08-31 22:49:58.732138','2023-08-31 22:49:58.732138',5,NULL),(48,'Aderezo',1,'2023-08-31 22:51:05.488135','2023-08-31 22:51:05.488135',12,NULL),(49,'Ajonjolí',1,'2023-08-31 22:52:34.935242','2023-08-31 22:52:34.935242',2,NULL),(50,'Bubaloo trueno pop',1,'2023-08-31 22:52:40.334177','2023-08-31 22:52:40.334177',2,NULL),(51,'Dragoncito',1,'2023-08-31 22:52:45.029453','2023-08-31 22:52:45.029453',2,NULL),(52,'Limoncito miguelito',1,'2023-08-31 22:52:49.236064','2023-08-31 22:52:49.236064',2,NULL),(53,'Mora trueno pop',1,'2023-08-31 22:52:53.086276','2023-08-31 22:52:53.086276',2,NULL),(54,'Súper miguelito',1,'2023-08-31 22:52:58.639942','2023-08-31 22:52:58.639942',2,NULL),(55,'Cebolla',1,'2023-08-31 22:53:27.602268','2023-08-31 22:53:27.602268',4,NULL),(56,'Jalapeño',1,'2023-08-31 22:53:33.778767','2023-08-31 22:53:33.778767',4,NULL),(57,'Jitomate',1,'2023-08-31 22:53:37.434022','2023-08-31 22:53:37.434022',4,NULL),(58,'Lechuga',1,'2023-08-31 22:53:46.113467','2023-08-31 22:53:46.113467',4,NULL),(59,'Queso',1,'2023-08-31 22:53:50.576751','2023-08-31 22:53:50.576751',6,NULL),(60,'Tocino',1,'2023-08-31 22:55:36.209335','2023-08-31 22:55:36.209335',3,NULL),(61,'Bubaloo xtream',1,'2023-08-31 22:56:01.706447','2023-08-31 22:56:01.706447',9,NULL),(62,'Limon crayón',1,'2023-08-31 22:56:06.745224','2023-08-31 22:56:06.745224',9,NULL),(63,'Mango crayón',1,'2023-08-31 22:56:11.562391','2023-08-31 22:56:11.562391',9,NULL),(64,'Mora crayón',1,'2023-08-31 22:56:15.702558','2023-08-31 22:56:15.702558',9,NULL),(65,'Pepino tamarindo',1,'2023-08-31 22:56:19.921149','2023-08-31 22:56:19.921149',9,NULL),(66,'Tamarindo natural',1,'2023-08-31 22:56:24.388299','2023-08-31 22:56:24.388299',9,NULL),(67,'Uva crayón',1,'2023-08-31 22:56:42.493003','2023-08-31 22:56:42.493003',9,NULL),(68,'Coca Cola',1,'2023-08-31 22:56:49.635155','2023-08-31 22:56:49.635155',10,NULL),(69,'Soda',1,'2023-08-31 23:02:06.841454','2023-08-31 23:02:06.841454',10,NULL),(70,'Agua mineral',1,'2023-08-31 23:02:12.138989','2023-08-31 23:02:12.138989',10,NULL),(71,'Chetos bolitas',1,'2023-08-31 23:02:33.076470','2023-08-31 23:02:33.076470',11,NULL),(72,'Chetos queso jalapeño',1,'2023-08-31 23:02:37.678022','2023-08-31 23:02:37.678022',11,NULL),(73,'Ruffles flamming hot',1,'2023-08-31 23:02:42.551276','2023-08-31 23:02:42.551276',11,NULL),(74,'Ruffles queso',1,'2023-08-31 23:02:49.624231','2023-08-31 23:02:49.624231',11,NULL),(75,'Pan buger',1,'2023-09-02 03:04:16.718855','2023-09-02 03:00:19.791365',12,NULL),(76,'Mostaza',1,'2023-09-02 03:01:56.308103','2023-09-02 03:01:56.308103',12,NULL),(77,'Mayonesa',1,'2023-09-02 03:02:02.800873','2023-09-02 03:02:02.800873',12,NULL),(78,'Catsup',1,'2023-09-02 03:03:05.995543','2023-09-02 03:03:05.995543',12,NULL),(79,'Pan jocho',1,'2023-09-02 03:04:26.423409','2023-09-02 03:04:26.423409',12,NULL);
/*!40000 ALTER TABLE `insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paquete`
--

DROP TABLE IF EXISTS `paquete`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paquete` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `tipo` int NOT NULL,
  `componentes` json DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `estatus` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `imagen` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paquete`
--

LOCK TABLES `paquete` WRITE;
/*!40000 ALTER TABLE `paquete` DISABLE KEYS */;
INSERT INTO `paquete` VALUES (5,'Burger + papas','',1,'[{\"id\": \"4\", \"nombre\": \"Buger pollo\", \"cantidad\": \"1\"}]',85.00,1,'2023-09-03 22:38:13.029454','2023-09-03 22:06:39.619331',NULL);
/*!40000 ALTER TABLE `paquete` ENABLE KEYS */;
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
  `breve` varchar(255) DEFAULT NULL,
  `tipo` int NOT NULL,
  `insumos` json DEFAULT NULL,
  `precio` decimal(10,2) NOT NULL,
  `estatus` int NOT NULL,
  `fecha_modificacion` datetime(6) NOT NULL,
  `fecha_alta` datetime(6) NOT NULL,
  `imagen` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Producto_nombre_c73d5e3f_uniq` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (4,'Buger pollo','',1,'[{\"id\": \"2\", \"opcion\": \"1\", \"nombre_grupo\": \"Carnes\", \"nombre_insumo\": \"Pollo\"}, {\"id\": \"60\", \"opcion\": \"3\", \"nombre_grupo\": \"Carnes\", \"nombre_insumo\": \"Tocino\"}, {\"id\": \"78\", \"opcion\": \"3\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Catsup\"}, {\"id\": \"77\", \"opcion\": \"3\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Mayonesa\"}, {\"id\": \"76\", \"opcion\": \"3\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Mostaza\"}, {\"id\": \"75\", \"opcion\": \"1\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Pan buger\"}, {\"id\": \"55\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Cebolla\"}, {\"id\": \"56\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Jalapeño\"}, {\"id\": \"57\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Jitomate\"}, {\"id\": \"58\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Lechuga\"}]',65.00,1,'2023-09-03 04:04:03.575574','2023-09-02 04:09:32.541542',NULL),(5,'Burger res','',1,'[{\"id\": \"1\", \"opcion\": \"1\", \"nombre_grupo\": \"Carnes\", \"nombre_insumo\": \"Res\"}, {\"id\": \"60\", \"opcion\": \"3\", \"nombre_grupo\": \"Carnes\", \"nombre_insumo\": \"Tocino\"}, {\"id\": \"78\", \"opcion\": \"3\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Catsup\"}, {\"id\": \"77\", \"opcion\": \"3\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Mayonesa\"}, {\"id\": \"76\", \"opcion\": \"3\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Mostaza\"}, {\"id\": \"75\", \"opcion\": \"1\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Pan buger\"}, {\"id\": \"55\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Cebolla\"}, {\"id\": \"56\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Jalapeño\"}, {\"id\": \"57\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Jitomate\"}, {\"id\": \"58\", \"opcion\": \"3\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Lechuga\"}]',65.00,1,'2023-09-03 04:04:55.993501','2023-09-02 04:18:43.162123',NULL),(6,'Jocho','',1,'[{\"id\": \"3\", \"opcion\": \"1\", \"nombre_grupo\": \"Carnes\", \"nombre_insumo\": \"Salchicha\"}, {\"id\": \"60\", \"opcion\": \"1\", \"nombre_grupo\": \"Carnes\", \"nombre_insumo\": \"Tocino\"}, {\"id\": \"78\", \"opcion\": \"1\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Catsup\"}, {\"id\": \"77\", \"opcion\": \"1\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Mayonesa\"}, {\"id\": \"76\", \"opcion\": \"1\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Mostaza\"}, {\"id\": \"79\", \"opcion\": \"1\", \"nombre_grupo\": \"Complemento comida\", \"nombre_insumo\": \"Pan jocho\"}, {\"id\": \"55\", \"opcion\": \"1\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Cebolla\"}, {\"id\": \"56\", \"opcion\": \"1\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Jalapeño\"}, {\"id\": \"57\", \"opcion\": \"1\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Jitomate\"}, {\"id\": \"58\", \"opcion\": \"1\", \"nombre_grupo\": \"Vegetales\", \"nombre_insumo\": \"Lechuga\"}]',50.00,1,'2023-09-02 04:19:43.874718','2023-09-02 04:19:43.874718',NULL);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'pbkdf2_sha256$320000$lOWdT1Dc9RukWr3MaDn58G$ZYu6w2CKDsmnKzrG861zDI4qSOSy8NWBkPQp03IxHqU=','2023-08-30 02:05:39.197462',1,'evallardy','','','evallardy@gmail.com',1,1,'2023-08-30 00:52:15.446354',NULL,0);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_user_permissions`
--

LOCK TABLES `usuario_user_permissions` WRITE;
/*!40000 ALTER TABLE `usuario_user_permissions` DISABLE KEYS */;
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

-- Dump completed on 2023-09-04 21:18:23
