-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 26-10-2022 a las 20:10:01
-- Versión del servidor: 5.7.36
-- Versión de PHP: 8.1.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `portafolio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_externo`
--

DROP TABLE IF EXISTS `cliente_externo`;
CREATE TABLE IF NOT EXISTS `cliente_externo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rut` varchar(30) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `empresa` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `cliente_externo`
--

INSERT INTO `cliente_externo` (`id`, `rut`, `nombre`, `apellido`, `empresa`) VALUES
(2, '22.222.222-2', 'Simon', 'Martinez', 'DuocUC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comerciante_local`
--

DROP TABLE IF EXISTS `comerciante_local`;
CREATE TABLE IF NOT EXISTS `comerciante_local` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rut` varchar(30) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `empresa` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `comerciante_local`
--

INSERT INTO `comerciante_local` (`id`, `rut`, `nombre`, `apellido`, `empresa`) VALUES
(1, '12.345.678-9', 'Jimmy', 'Martinez', 'DuocUC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productor`
--

DROP TABLE IF EXISTS `productor`;
CREATE TABLE IF NOT EXISTS `productor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rut` varchar(30) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `empresa` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `productor`
--

INSERT INTO `productor` (`id`, `rut`, `nombre`, `apellido`, `empresa`) VALUES
(1, '19.985.094-6', 'Kevin', 'Martinez', 'DuocUC'),
(2, '11.111.111-1', 'Emerson', 'Meneses', 'DuocUC'),
(6, '22.222.222-2', 'Lukas', 'Sanhueza', 'DuocUC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(30) NOT NULL,
  `passwd` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `user`, `passwd`) VALUES
(1, 'kevin', 'martinez'),
(2, 'admin', 'admin');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
