SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema st
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema st
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `st` DEFAULT CHARACTER SET utf8 ;
USE `st` ;

-- -----------------------------------------------------
-- Table `st`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Cliente` (
  `Codigo_Cliente` INT NOT NULL AUTO_INCREMENT,
  `Cedula` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Fecha_Nacimiento` DATE NOT NULL,
  `Telefono` VARCHAR(45) NOT NULL,
  `Direccion` VARCHAR(45) NOT NULL,
  `Movil` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Codigo_Cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Talla`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Talla` (
  `Codigo_Talla` INT NOT NULL AUTO_INCREMENT,
  `Numero` VARCHAR(45) NOT NULL,
  `Letra` VARCHAR(45) NULL,
  PRIMARY KEY (`Codigo_Talla`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Color`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Color` (
  `Codigo_Color` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Referencia` VARCHAR(45) NULL,
  PRIMARY KEY (`Codigo_Color`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Estilo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Estilo` (
  `Codigo_Estilo` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Codigo_Estilo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Tela`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Tela` (
  `Codigo_Tela` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`Codigo_Tela`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Estampado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Estampado` (
  `Codigo_Estampado` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Imagen` VARCHAR(45) NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`Codigo_Estampado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Producto` (
  `Codigo_Producto` INT NOT NULL AUTO_INCREMENT,
  `Codigo_Tela` INT NOT NULL,
  `Codigo_Estilo` INT NOT NULL,
  `Codigo_Talla` INT NOT NULL,
  `Codigo_Color` INT NOT NULL,
  `Codigo_Estampado` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Precio` INT NOT NULL,
  `Stock` INT NOT NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`Codigo_Producto`),
  INDEX `fk_Producto_Talla1_idx` (`Codigo_Talla` ASC),
  INDEX `fk_Producto_Color1_idx` (`Codigo_Color` ASC),
  INDEX `fk_Producto_Estilo1_idx` (`Codigo_Estilo` ASC),
  INDEX `fk_Producto_Tipo_Tela1_idx` (`Codigo_Tela` ASC),
  INDEX `fk_Producto_Estampado1_idx` (`Codigo_Estampado` ASC),
  CONSTRAINT `fk_Producto_Talla1`
    FOREIGN KEY (`Codigo_Talla`)
    REFERENCES `st`.`Talla` (`Codigo_Talla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Color1`
    FOREIGN KEY (`Codigo_Color`)
    REFERENCES `st`.`Color` (`Codigo_Color`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Estilo1`
    FOREIGN KEY (`Codigo_Estilo`)
    REFERENCES `st`.`Estilo` (`Codigo_Estilo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Tipo_Tela1`
    FOREIGN KEY (`Codigo_Tela`)
    REFERENCES `st`.`Tela` (`Codigo_Tela`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Estampado1`
    FOREIGN KEY (`Codigo_Estampado`)
    REFERENCES `st`.`Estampado` (`Codigo_Estampado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Empleado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Empleado` (
  `Codigo_Empleado` INT NOT NULL AUTO_INCREMENT,
  `Cedula` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Fecha_Nacimiento` DATE NOT NULL,
  `Fecha_Contratacion` DATE NOT NULL,
  `Telefono` VARCHAR(45) NOT NULL,
  `Direccion` VARCHAR(45) NOT NULL,
  `Movil` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Codigo_Empleado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Factura` (
  `Codigo_Factura` INT NOT NULL AUTO_INCREMENT,
  `Codigo_Cliente` INT NOT NULL,
  `Codigo_Empleado` INT NOT NULL,
  `Fecha` DATE NOT NULL,
  `Total` DOUBLE NOT NULL,
  PRIMARY KEY (`Codigo_Factura`),
  INDEX `fk_Movimiento_Persona1_idx` (`Codigo_Cliente` ASC),
  INDEX `fk_Factura_Vendedor1_idx` (`Codigo_Empleado` ASC),
  CONSTRAINT `fk_Movimiento_Persona1`
    FOREIGN KEY (`Codigo_Cliente`)
    REFERENCES `st`.`Cliente` (`Codigo_Cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_Vendedor1`
    FOREIGN KEY (`Codigo_Empleado`)
    REFERENCES `st`.`Empleado` (`Codigo_Empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Insumo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Insumo` (
  `Codigo_Insumo` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Referencia` VARCHAR(45) NOT NULL,
  `Tipo` VARCHAR(45) NOT NULL,
  `Fecha_Compra` DATE NOT NULL,
  `Fecha_Vencimiento` DATE NOT NULL,
  PRIMARY KEY (`Codigo_Insumo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Compra` (
  `Codigo_Compra` INT NOT NULL AUTO_INCREMENT,
  `Codigo_Insumo` INT NOT NULL,
  `Codigo_Empleado` INT NOT NULL,
  `Cantidad` VARCHAR(45) NOT NULL,
  `Precio` DOUBLE NOT NULL,
  `Fecha` DATE NOT NULL,
  INDEX `fk_Producto_has_Insumo_Insumo1_idx` (`Codigo_Insumo` ASC),
  PRIMARY KEY (`Codigo_Compra`),
  INDEX `fk_Compra_Vendedor1_idx` (`Codigo_Empleado` ASC),
  CONSTRAINT `fk_Producto_has_Insumo_Insumo1`
    FOREIGN KEY (`Codigo_Insumo`)
    REFERENCES `st`.`Insumo` (`Codigo_Insumo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Compra_Vendedor1`
    FOREIGN KEY (`Codigo_Empleado`)
    REFERENCES `st`.`Empleado` (`Codigo_Empleado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Venta` (
  `Codigo_Venta` INT NOT NULL AUTO_INCREMENT,
  `Codigo_Factura` INT NOT NULL,
  `Codigo_Producto` INT NOT NULL,
  `Cantidad` VARCHAR(45) NOT NULL,
  `Precio` DOUBLE NOT NULL,
  PRIMARY KEY (`Codigo_Venta`),
  INDEX `fk_MovimientoProducto_Movimiento1_idx` (`Codigo_Factura` ASC),
  INDEX `fk_MovimientoProducto_Producto1_idx` (`Codigo_Producto` ASC),
  CONSTRAINT `fk_MovimientoProducto_Movimiento1`
    FOREIGN KEY (`Codigo_Factura`)
    REFERENCES `st`.`Factura` (`Codigo_Factura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MovimientoProducto_Producto1`
    FOREIGN KEY (`Codigo_Producto`)
    REFERENCES `st`.`Producto` (`Codigo_Producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Detalle`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Detalle` (
  `Codigo_Detalle` INT NOT NULL AUTO_INCREMENT,
  `Codigo_Producto` INT NOT NULL,
  `Codigo_Insumo` INT NOT NULL,
  `Descripcion` VARCHAR(45) NOT NULL,
  `Referencia` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Codigo_Detalle`),
  INDEX `fk_Detalle_Producto1_idx` (`Codigo_Producto` ASC),
  INDEX `fk_Detalle_Insumo1_idx` (`Codigo_Insumo` ASC),
  CONSTRAINT `fk_Detalle_Producto1`
    FOREIGN KEY (`Codigo_Producto`)
    REFERENCES `st`.`Producto` (`Codigo_Producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Detalle_Insumo1`
    FOREIGN KEY (`Codigo_Insumo`)
    REFERENCES `st`.`Insumo` (`Codigo_Insumo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
