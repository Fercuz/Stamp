
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `st` DEFAULT CHARACTER SET utf8 ;
USE `st` ;

-- -----------------------------------------------------
-- Table `st`.`Perfil`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Perfil` (
  `Cod_Perfil` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Cod_Perfil`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Persona` (
  `Cod_Persona` INT NOT NULL AUTO_INCREMENT,
  `Cod_Perfil` INT NOT NULL,
  `Cedula` VARCHAR(45) NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  `Fecha_Nacimiento` DATE NOT NULL,
  `Telefono` VARCHAR(45) NOT NULL,
  `Direccion` VARCHAR(45) NOT NULL,
  `Movil` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Cod_Persona`),
  INDEX `fk_Persona_Perfil1_idx` (`Cod_Perfil` ASC),
  CONSTRAINT `fk_Persona_Perfil1`
    FOREIGN KEY (`Cod_Perfil`)
    REFERENCES `st`.`Perfil` (`Cod_Perfil`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Marca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Marca` (
  `Cod_Marca` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Cod_Marca`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Talla`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Talla` (
  `Cod_Talla` INT NOT NULL AUTO_INCREMENT,
  `Numero` VARCHAR(45) NOT NULL,
  `Letra` VARCHAR(45) NULL,
  PRIMARY KEY (`Cod_Talla`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Color`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Color` (
  `Cod_Color` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Referencia` VARCHAR(45) NULL,
  PRIMARY KEY (`Cod_Color`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Estilo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Estilo` (
  `Cod_Estilo` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Cod_Estilo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Tela`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Tela` (
  `Cod_Tela` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`Cod_Tela`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Estampado`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Estampado` (
  `Cod_Estampado` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`Cod_Estampado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Producto` (
  `Cod_Producto` INT NOT NULL AUTO_INCREMENT,
  `Cod_Estampado` INT NOT NULL,
  `Cod_Tela` INT NOT NULL,
  `Cod_Marca` INT NOT NULL,
  `Cod_Talla` INT NOT NULL,
  `Cod_Color` INT NOT NULL,
  `Cod_Estilo` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Valor_Venta` INT NOT NULL,
  `Valor_Produccion` INT NOT NULL,
  `Cantidad_Existente` INT NOT NULL,
  `Stock_Minimo` INT NOT NULL,
  `Stock_Maximo` INT NOT NULL,
  `Descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`Cod_Producto`),
  INDEX `fk_Producto_Marca1_idx` (`Cod_Marca` ASC),
  INDEX `fk_Producto_Talla1_idx` (`Cod_Talla` ASC),
  INDEX `fk_Producto_Color1_idx` (`Cod_Color` ASC),
  INDEX `fk_Producto_Estilo1_idx` (`Cod_Estilo` ASC),
  INDEX `fk_Producto_Tipo_Tela1_idx` (`Cod_Tela` ASC),
  INDEX `fk_Producto_Estampado1_idx` (`Cod_Estampado` ASC),
  CONSTRAINT `fk_Producto_Marca1`
    FOREIGN KEY (`Cod_Marca`)
    REFERENCES `st`.`Marca` (`Cod_Marca`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Talla1`
    FOREIGN KEY (`Cod_Talla`)
    REFERENCES `st`.`Talla` (`Cod_Talla`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Color1`
    FOREIGN KEY (`Cod_Color`)
    REFERENCES `st`.`Color` (`Cod_Color`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Estilo1`
    FOREIGN KEY (`Cod_Estilo`)
    REFERENCES `st`.`Estilo` (`Cod_Estilo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Tipo_Tela1`
    FOREIGN KEY (`Cod_Tela`)
    REFERENCES `st`.`Tela` (`Cod_Tela`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Producto_Estampado1`
    FOREIGN KEY (`Cod_Estampado`)
    REFERENCES `st`.`Estampado` (`Cod_Estampado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Venta` (
  `Cod_Venta` INT NOT NULL AUTO_INCREMENT,
  `Cod_Persona` INT NOT NULL,
  `Fecha_Movimiento` DATE NOT NULL,
  `Monto` DOUBLE NOT NULL,
  PRIMARY KEY (`Cod_Venta`),
  INDEX `fk_Movimiento_Persona1_idx` (`Cod_Persona` ASC),
  CONSTRAINT `fk_Movimiento_Persona1`
    FOREIGN KEY (`Cod_Persona`)
    REFERENCES `st`.`Persona` (`Cod_Persona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`Insumo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`Insumo` (
  `Cod_Insumo` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Referencia` VARCHAR(45) NOT NULL,
  `Tipo` VARCHAR(45) NOT NULL,
  `Fecha_Compra` DATE NOT NULL,
  `Fecha_Vencimiento` DATE NOT NULL,
  PRIMARY KEY (`Cod_Insumo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`CompraInsumo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`CompraInsumo` (
  `Cod_Compra_Insumo` INT NOT NULL AUTO_INCREMENT,
  `Cod_Insumo` INT NOT NULL,
  `Cod_Persona` INT NOT NULL,
  `Cantidad` VARCHAR(45) NOT NULL,
  `Valor` DOUBLE NOT NULL,
  PRIMARY KEY (`Cod_Compra_Insumo`),
  INDEX `fk_MovimientoInsumo_Insumo1_idx` (`Cod_Insumo` ASC),
  INDEX `fk_CompraInsumo_Persona1_idx` (`Cod_Persona` ASC),
  CONSTRAINT `fk_MovimientoInsumo_Insumo1`
    FOREIGN KEY (`Cod_Insumo`)
    REFERENCES `st`.`Insumo` (`Cod_Insumo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CompraInsumo_Persona1`
    FOREIGN KEY (`Cod_Persona`)
    REFERENCES `st`.`Persona` (`Cod_Persona`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`InsumoProducto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`InsumoProducto` (
  `Cod_Insumo_Producto` INT NOT NULL AUTO_INCREMENT,
  `Cod_Producto` INT NOT NULL,
  `Cod_Insumo` INT NOT NULL,
  `Cantidad` VARCHAR(45) NOT NULL,
  `Valor` DOUBLE NOT NULL,
  INDEX `fk_Producto_has_Insumo_Insumo1_idx` (`Cod_Insumo` ASC),
  PRIMARY KEY (`Cod_Insumo_Producto`),
  INDEX `fk_InsumoProducto_Producto1_idx` (`Cod_Producto` ASC),
  CONSTRAINT `fk_Producto_has_Insumo_Insumo1`
    FOREIGN KEY (`Cod_Insumo`)
    REFERENCES `st`.`Insumo` (`Cod_Insumo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_InsumoProducto_Producto1`
    FOREIGN KEY (`Cod_Producto`)
    REFERENCES `st`.`Producto` (`Cod_Producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `st`.`VentaProducto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `st`.`VentaProducto` (
  `Cod_Venta_Producto` INT NOT NULL AUTO_INCREMENT,
  `Cod_Venta` INT NOT NULL,
  `Cod_Producto` INT NOT NULL,
  `Cantidad` VARCHAR(45) NOT NULL,
  `Valor` DOUBLE NOT NULL,
  PRIMARY KEY (`Cod_Venta_Producto`),
  INDEX `fk_MovimientoProducto_Movimiento1_idx` (`Cod_Venta` ASC),
  INDEX `fk_MovimientoProducto_Producto1_idx` (`Cod_Producto` ASC),
  CONSTRAINT `fk_MovimientoProducto_Movimiento1`
    FOREIGN KEY (`Cod_Venta`)
    REFERENCES `st`.`Venta` (`Cod_Venta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MovimientoProducto_Producto1`
    FOREIGN KEY (`Cod_Producto`)
    REFERENCES `st`.`Producto` (`Cod_Producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
