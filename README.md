# Proyecto de Gestión de Precios de Entradas en Tiempo Real

Este proyecto es una prueba de concepto que utiliza Docker, Kafka, Redis y Python para crear una aplicación que genera eventos, como la publicación de un nuevo precio de una entrada, y que las aplicaciones cliente los reciban. Estos estarán disponibles en caché hasta que venga un nuevo precio de entrada, en que refrescarán dichos valores e informará a las aplicaciones cliente.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Proyecto](#configuración-del-proyecto)
- [Servicios](#servicios)
- [Acceso a las Herramientas](#acceso-a-las-herramientas)
- [Arrancar la aplicación](#arrancar-la-aplicación)

## Requisitos

- Docker
- Docker Compose

## Configuración del Proyecto

1. Clona el repositorio:
   ```sh
   git clone https://github.com/DavidFP/Tickets.git
   cd Tickets
   
## Servicios
El archivo docker-compose.yml configura los siguientes servicios:

- zookeeper: Servicio Zookeeper para coordinar Kafka.
- kafka: Servicio Kafka para gestionar la cola de mensajes.
- redis: Servicio Redis para almacenamiento en caché.
- producer: Servicio productor que genera eventos de precios de entradas.
- consumer: Servicio consumidor que procesa los eventos de precios de entradas.
- web: Servicio web basado en Flask que muestra los precios de entradas en tiempo real.
- kafka-ui: Interfaz de usuario para gestionar Kafka.
- redis-commander: Interfaz de usuario para gestionar Redis.

## Acceso a las Herramientas
- Aplicación web: http://localhost:5001
- Kafka UI: http://localhost:8080
- Redis Commander: http://localhost:8001

## Arrancar la aplicación
```sh
docker-compose up --build


