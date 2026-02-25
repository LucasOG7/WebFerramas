SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `ferramas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `id_pedido` int(255) NOT NULL,
  `nom_pedido` varchar(255) DEFAULT NULL,
  `desc_pedido` varchar(255) DEFAULT NULL,
  `precio_pedido` int(9) DEFAULT NULL,
  `cantidad` int(11) NOT NULL,
  `id_user` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`id_pedido`, `nom_pedido`, `desc_pedido`, `precio_pedido`, `cantidad`, `id_user`) VALUES
(100, 'Martillo', 'Herramienta de mano', 19990, 3, 0),
(0, 'Caja de Clavos', 'Pieza metálica, larga y delgada, con cabeza y punt', 5990, 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tools`
--

CREATE TABLE `tools` (
  `id_tool` int(11) NOT NULL,
  `id_tools_type` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tools`
--

INSERT INTO `tools` (`id_tool`, `id_tools_type`, `name`, `description`, `stock`, `precio`) VALUES
(100, 1, 'Martillo', 'Herramienta de mano', 100, 19990),
(110, 2, 'Caja de Clavos', 'Pieza metálica, larga y delgada, con cabeza y punt', 100, 5990),
(120, 3, 'Casco de seguridad', 'Protección', 50, 3990);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tools_type`
--

CREATE TABLE `tools_type` (
  `id` int(11) DEFAULT NULL,
  `des` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tools_type`
--

INSERT INTO `tools_type` (`id`, `des`) VALUES
(1000, 'Manuales'),
(1001, 'Electricas'),
(1000, 'Manuales'),
(1001, 'Electricas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id_user` int(5) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `contraseña` varchar(255) NOT NULL,
  `verificar_contraseña` varchar(255) NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `descuento` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id_user`, `correo`, `contraseña`, `verificar_contraseña`, `usuario`, `descuento`) VALUES
(12, 'asd@asd', 'asd', '', 'asd', 0),
(13, 'zxc@zx', 'zxc', '', 'zxc', 0),
(14, 'qqqq@qqqq', 'qq', '', 'qqq', 0),
(15, 'tttt@ttt', 't', '', 'ttt', 0),
(16, 'desc@desc', 'desc', '', 'desc', 0),
(17, 'ccc@cccc', 'cc', '', 'ccc', 0);

--
-- �?ndices para tablas volcadas
--

--
-- Indices de la tabla `tools`
--
ALTER TABLE `tools`
  ADD PRIMARY KEY (`id_tool`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tools`
--
ALTER TABLE `tools`
  MODIFY `id_tool` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
