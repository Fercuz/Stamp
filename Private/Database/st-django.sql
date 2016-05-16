-- phpMyAdmin SQL Dump
-- version 4.5.1
-- Versión de PHP: 7.0.5
-- root / root123

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `st` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `st`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add Color', 7, 'add_color'),
(20, 'Can change Color', 7, 'change_color'),
(21, 'Can delete Color', 7, 'delete_color'),
(22, 'Can add Compra de Insumo', 8, 'add_comprainsumo'),
(23, 'Can change Compra de Insumo', 8, 'change_comprainsumo'),
(24, 'Can delete Compra de Insumo', 8, 'delete_comprainsumo'),
(25, 'Can add django migrations', 9, 'add_djangomigrations'),
(26, 'Can change django migrations', 9, 'change_djangomigrations'),
(27, 'Can delete django migrations', 9, 'delete_djangomigrations'),
(28, 'Can add Estampado', 10, 'add_estampado'),
(29, 'Can change Estampado', 10, 'change_estampado'),
(30, 'Can delete Estampado', 10, 'delete_estampado'),
(31, 'Can add Estilo', 11, 'add_estilo'),
(32, 'Can change Estilo', 11, 'change_estilo'),
(33, 'Can delete Estilo', 11, 'delete_estilo'),
(34, 'Can add Insumo', 12, 'add_insumo'),
(35, 'Can change Insumo', 12, 'change_insumo'),
(36, 'Can delete Insumo', 12, 'delete_insumo'),
(37, 'Can add Insumo Producto', 13, 'add_insumoproducto'),
(38, 'Can change Insumo Producto', 13, 'change_insumoproducto'),
(39, 'Can delete Insumo Producto', 13, 'delete_insumoproducto'),
(40, 'Can add Marca', 14, 'add_marca'),
(41, 'Can change Marca', 14, 'change_marca'),
(42, 'Can delete Marca', 14, 'delete_marca'),
(43, 'Can add Perfil', 15, 'add_perfil'),
(44, 'Can change Perfil', 15, 'change_perfil'),
(45, 'Can delete Perfil', 15, 'delete_perfil'),
(46, 'Can add Persona', 16, 'add_persona'),
(47, 'Can change Persona', 16, 'change_persona'),
(48, 'Can delete Persona', 16, 'delete_persona'),
(49, 'Can add Producto', 17, 'add_producto'),
(50, 'Can change Producto', 17, 'change_producto'),
(51, 'Can delete Producto', 17, 'delete_producto'),
(52, 'Can add Talla', 18, 'add_talla'),
(53, 'Can change Talla', 18, 'change_talla'),
(54, 'Can delete Talla', 18, 'delete_talla'),
(55, 'Can add Tela', 19, 'add_tela'),
(56, 'Can change Tela', 19, 'change_tela'),
(57, 'Can delete Tela', 19, 'delete_tela'),
(58, 'Can add Venta', 20, 'add_venta'),
(59, 'Can change Venta', 20, 'change_venta'),
(60, 'Can delete Venta', 20, 'delete_venta'),
(61, 'Can add Venta de Producto', 21, 'add_ventaproducto'),
(62, 'Can change Venta de Producto', 21, 'change_ventaproducto'),
(63, 'Can delete Venta de Producto', 21, 'delete_ventaproducto');

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(2, 'pbkdf2_sha256$24000$FmduJRpk1Vt2$6RWy9wsMDsROJiydSaWNmXEikn4/NQhmvuiJ8HBN74U=', NULL, 1, 'root', '', '', 'admin@admin.com', 1, 1, '2016-05-14 16:59:13');

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `color` (
  `Cod_Color` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Referencia` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `comprainsumo` (
  `Cod_Compra_Insumo` int(11) NOT NULL,
  `Cod_Insumo` int(11) NOT NULL,
  `Cod_Persona` int(11) NOT NULL,
  `Cantidad` varchar(45) NOT NULL,
  `Valor` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'Stamping', 'color'),
(8, 'Stamping', 'comprainsumo'),
(9, 'Stamping', 'djangomigrations'),
(10, 'Stamping', 'estampado'),
(11, 'Stamping', 'estilo'),
(12, 'Stamping', 'insumo'),
(13, 'Stamping', 'insumoproducto'),
(14, 'Stamping', 'marca'),
(15, 'Stamping', 'perfil'),
(16, 'Stamping', 'persona'),
(17, 'Stamping', 'producto'),
(18, 'Stamping', 'talla'),
(19, 'Stamping', 'tela'),
(20, 'Stamping', 'venta'),
(21, 'Stamping', 'ventaproducto');

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2016-05-14 15:42:29'),
(2, 'auth', '0001_initial', '2016-05-14 15:42:34'),
(3, 'admin', '0001_initial', '2016-05-14 15:42:35'),
(4, 'admin', '0002_logentry_remove_auto_add', '2016-05-14 15:42:35'),
(5, 'contenttypes', '0002_remove_content_type_name', '2016-05-14 15:42:36'),
(6, 'auth', '0002_alter_permission_name_max_length', '2016-05-14 15:42:37'),
(7, 'auth', '0003_alter_user_email_max_length', '2016-05-14 15:42:38'),
(8, 'auth', '0004_alter_user_username_opts', '2016-05-14 15:42:38'),
(9, 'auth', '0005_alter_user_last_login_null', '2016-05-14 15:42:38'),
(10, 'auth', '0006_require_contenttypes_0002', '2016-05-14 15:42:38'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2016-05-14 15:42:38'),
(12, 'sessions', '0001_initial', '2016-05-14 15:42:39');

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4vy07ow1i32xu9xm7li1wf8nhrapt8nk', 'Y2I0ZTg3MTdlZjBjMDk2Yzk4ODUzNzY5ZDc1YTFkOGIyZDI3MGVmZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZTdmZjcyYzYyMTAxYTdlMDZlNWNhN2EzZGI5ZjczYTFmZjZjZjdmYiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2016-05-28 15:45:01'),
('kjri8oz19m719zzf3gc3p5hazgjm82zs', 'MjEwNmNkN2JjNGI3YzExOWQxODE4ZGE2ZjcxNjRiZWE4YTAxNmFjMzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlN2ZmNzJjNjIxMDFhN2UwNmU1Y2E3YTNkYjlmNzNhMWZmNmNmN2ZiIn0=', '2016-05-28 16:46:28');

CREATE TABLE `estampado` (
  `Cod_Estampado` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `estilo` (
  `Cod_Estilo` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `insumo` (
  `Cod_Insumo` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Referencia` varchar(45) NOT NULL,
  `Tipo` varchar(45) NOT NULL,
  `Fecha_Compra` date NOT NULL,
  `Fecha_Vencimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `insumoproducto` (
  `Cod_Insumo_Producto` int(11) NOT NULL,
  `Cod_Producto` int(11) NOT NULL,
  `Cod_Insumo` int(11) NOT NULL,
  `Cantidad` varchar(45) NOT NULL,
  `Valor` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `marca` (
  `Cod_Marca` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `perfil` (
  `Cod_Perfil` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `persona` (
  `Cod_Persona` int(11) NOT NULL,
  `Cod_Perfil` int(11) NOT NULL,
  `Cedula` varchar(45) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `Fecha_Nacimiento` date NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Movil` varchar(45) DEFAULT NULL,
  `Email` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `producto` (
  `Cod_Producto` int(11) NOT NULL,
  `Cod_Estampado` int(11) NOT NULL,
  `Cod_Tela` int(11) NOT NULL,
  `Cod_Marca` int(11) NOT NULL,
  `Cod_Talla` int(11) NOT NULL,
  `Cod_Color` int(11) NOT NULL,
  `Cod_Estilo` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Valor_Venta` int(11) NOT NULL,
  `Valor_Produccion` int(11) NOT NULL,
  `Cantidad_Existente` int(11) NOT NULL,
  `Stock_Minimo` int(11) NOT NULL,
  `Stock_Maximo` int(11) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `talla` (
  `Cod_Talla` int(11) NOT NULL,
  `Numero` varchar(45) NOT NULL,
  `Letra` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `tela` (
  `Cod_Tela` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Descripcion` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `venta` (
  `Cod_Venta` int(11) NOT NULL,
  `Cod_Persona` int(11) NOT NULL,
  `Fecha_Movimiento` date NOT NULL,
  `Monto` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `ventaproducto` (
  `Cod_Venta_Producto` int(11) NOT NULL,
  `Cod_Venta` int(11) NOT NULL,
  `Cod_Producto` int(11) NOT NULL,
  `Cantidad` varchar(45) NOT NULL,
  `Valor` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`);

ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`);

ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`);

ALTER TABLE `color`
  ADD PRIMARY KEY (`Cod_Color`);

ALTER TABLE `comprainsumo`
  ADD PRIMARY KEY (`Cod_Compra_Insumo`),
  ADD KEY `fk_MovimientoInsumo_Insumo1_idx` (`Cod_Insumo`),
  ADD KEY `fk_CompraInsumo_Persona1_idx` (`Cod_Persona`);

ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`);

ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

ALTER TABLE `estampado`
  ADD PRIMARY KEY (`Cod_Estampado`);

ALTER TABLE `estilo`
  ADD PRIMARY KEY (`Cod_Estilo`);

ALTER TABLE `insumo`
  ADD PRIMARY KEY (`Cod_Insumo`);

ALTER TABLE `insumoproducto`
  ADD PRIMARY KEY (`Cod_Insumo_Producto`),
  ADD KEY `fk_Producto_has_Insumo_Insumo1_idx` (`Cod_Insumo`),
  ADD KEY `fk_InsumoProducto_Producto1_idx` (`Cod_Producto`);

ALTER TABLE `marca`
  ADD PRIMARY KEY (`Cod_Marca`);

ALTER TABLE `perfil`
  ADD PRIMARY KEY (`Cod_Perfil`);

ALTER TABLE `persona`
  ADD PRIMARY KEY (`Cod_Persona`),
  ADD KEY `fk_Persona_Perfil1_idx` (`Cod_Perfil`);

ALTER TABLE `producto`
  ADD PRIMARY KEY (`Cod_Producto`),
  ADD KEY `fk_Producto_Marca1_idx` (`Cod_Marca`),
  ADD KEY `fk_Producto_Talla1_idx` (`Cod_Talla`),
  ADD KEY `fk_Producto_Color1_idx` (`Cod_Color`),
  ADD KEY `fk_Producto_Estilo1_idx` (`Cod_Estilo`),
  ADD KEY `fk_Producto_Tipo_Tela1_idx` (`Cod_Tela`),
  ADD KEY `fk_Producto_Estampado1_idx` (`Cod_Estampado`);

ALTER TABLE `talla`
  ADD PRIMARY KEY (`Cod_Talla`);

ALTER TABLE `tela`
  ADD PRIMARY KEY (`Cod_Tela`);

ALTER TABLE `venta`
  ADD PRIMARY KEY (`Cod_Venta`),
  ADD KEY `fk_Movimiento_Persona1_idx` (`Cod_Persona`);

ALTER TABLE `ventaproducto`
  ADD PRIMARY KEY (`Cod_Venta_Producto`),
  ADD KEY `fk_MovimientoProducto_Movimiento1_idx` (`Cod_Venta`),
  ADD KEY `fk_MovimientoProducto_Producto1_idx` (`Cod_Producto`);

ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `color`
  MODIFY `Cod_Color` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `comprainsumo`
  MODIFY `Cod_Compra_Insumo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

ALTER TABLE `estampado`
  MODIFY `Cod_Estampado` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `estilo`
  MODIFY `Cod_Estilo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `insumo`
  MODIFY `Cod_Insumo` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `insumoproducto`
  MODIFY `Cod_Insumo_Producto` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `marca`
  MODIFY `Cod_Marca` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `perfil`
  MODIFY `Cod_Perfil` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `persona`
  MODIFY `Cod_Persona` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `producto`
  MODIFY `Cod_Producto` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `talla`
  MODIFY `Cod_Talla` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `tela`
  MODIFY `Cod_Tela` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `venta`
  MODIFY `Cod_Venta` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `ventaproducto`
  MODIFY `Cod_Venta_Producto` int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `comprainsumo`
  ADD CONSTRAINT `fk_CompraInsumo_Persona1` FOREIGN KEY (`Cod_Persona`) REFERENCES `persona` (`Cod_Persona`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_MovimientoInsumo_Insumo1` FOREIGN KEY (`Cod_Insumo`) REFERENCES `insumo` (`Cod_Insumo`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

ALTER TABLE `insumoproducto`
  ADD CONSTRAINT `fk_InsumoProducto_Producto1` FOREIGN KEY (`Cod_Producto`) REFERENCES `producto` (`Cod_Producto`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Producto_has_Insumo_Insumo1` FOREIGN KEY (`Cod_Insumo`) REFERENCES `insumo` (`Cod_Insumo`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `persona`
  ADD CONSTRAINT `fk_Persona_Perfil1` FOREIGN KEY (`Cod_Perfil`) REFERENCES `perfil` (`Cod_Perfil`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `producto`
  ADD CONSTRAINT `fk_Producto_Color1` FOREIGN KEY (`Cod_Color`) REFERENCES `color` (`Cod_Color`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Producto_Estampado1` FOREIGN KEY (`Cod_Estampado`) REFERENCES `estampado` (`Cod_Estampado`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Producto_Estilo1` FOREIGN KEY (`Cod_Estilo`) REFERENCES `estilo` (`Cod_Estilo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Producto_Marca1` FOREIGN KEY (`Cod_Marca`) REFERENCES `marca` (`Cod_Marca`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Producto_Talla1` FOREIGN KEY (`Cod_Talla`) REFERENCES `talla` (`Cod_Talla`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_Producto_Tipo_Tela1` FOREIGN KEY (`Cod_Tela`) REFERENCES `tela` (`Cod_Tela`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `venta`
  ADD CONSTRAINT `fk_Movimiento_Persona1` FOREIGN KEY (`Cod_Persona`) REFERENCES `persona` (`Cod_Persona`) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE `ventaproducto`
  ADD CONSTRAINT `fk_MovimientoProducto_Movimiento1` FOREIGN KEY (`Cod_Venta`) REFERENCES `venta` (`Cod_Venta`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_MovimientoProducto_Producto1` FOREIGN KEY (`Cod_Producto`) REFERENCES `producto` (`Cod_Producto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

