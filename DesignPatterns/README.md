<a name="top"></a>
# Dessign Patterns
En el camino a convertirme en un mejor Ingeniero de SW, este proyecto tiene la finalidad de estudiar los 
patrones de diseño más utilizados en el mundo de la ingeniería del software.

En este proyecto, estudiaremos:

* [Qué es un patron de diseño](#item1)
* [Clasificación de los patrones de diseño](#item2)
  * [Patrones Creacionales](#item3)
    * [Factory](#Factory)
    * [Abstract Factory](#AbstractFactory)
    * [Builder](#Builder)
    * Prototype
    * Singleton
  * Patrones Estructurales
    * Adapter
    * Bridge
    * Composite
    * Decorator
    * Farcade
    * Flyweight
    * Proxy
  * Patrones de Comportamiento
    * Chain of Responsibility
    * Command
    * Iterator
    * Mediator
    * Memento
    * Observer
    * State
    * Strategy
    * Template Method
    * Visitor
* Ejemplos de código

Toda la información aqui contenida ha sido obtenida de https://refactoring.guru/es/design*patterns .

Este proyecto forma parte de un proyecto mas grande, denominado "SW Engineering Roadmap", en el cual estudiaremos todos
los casos contenidos dentro del famoso repositorio de GitHub "Coding Interview University" (https://github.com/jwasham/coding*interview*university).

<a name="item1"></a>

## What is a Design Pattern

Los patrones de diseño son soluciones habituales a problemas que ocurren con frecuencia en el diseño de software. Son como planos prefabricados que se pueden personalizar para resolver un problema de diseño recurrente en tu código.

No se puede elegir un patrón y copiarlo en el programa como si se tratara de funciones o bibliotecas ya preparadas. El patrón no es una porción específica de código, sino un concepto general para resolver un problema particular. Puedes seguir los detalles del patrón e implementar una solución que encaje con las realidades de tu propio programa.

A menudo los patrones se confunden con algoritmos porque ambos conceptos describen soluciones típicas a problemas conocidos. Mientras que un algoritmo siempre define un grupo claro de acciones para lograr un objetivo, un patrón es una descripción de más alto nivel de una solución. El código del mismo patrón aplicado a dos programas distintos puede ser diferente.

Una analogía de un algoritmo sería una receta de cocina: ambos cuentan con pasos claros para alcanzar una meta. Por su parte, un patrón es más similar a un plano, ya que puedes observar cómo son su resultado y sus funciones, pero el orden exacto de la implementación depende de ti.

### ¿En qué consiste el patrón?
La mayoría de los patrones se describe con mucha formalidad para que la gente pueda reproducirlos en muchos contextos. Aquí tienes las secciones que suelen estar presentes en la descripción de un patrón:

El propósito del patrón explica brevemente el problema y la solución.
La motivación explica en más detalle el problema y la solución que brinda el patrón.
La estructura de las clases muestra cada una de las partes del patrón y el modo en que se relacionan.
El ejemplo de código en uno de los lenguajes de programación populares facilita la asimilación de la idea que se esconde tras el patrón.
Algunos catálogos de patrones enumeran otros detalles útiles, como la aplicabilidad del patrón, los pasos de implementación y las relaciones con otros patrones.

<a name="item2"></a>

## Clasificación de los patrones de diseño

Los patrones de diseño varían en su complejidad, nivel de detalle y escala de aplicabilidad al sistema completo que se diseña. Me gusta la analogía de la construcción de carreteras: puedes hacer más segura una intersección instalando semáforos o construyendo un intercambiador completo de varios niveles con pasajes subterráneos para peatones.

Los patrones más básicos y de más bajo nivel suelen llamarse idioms. Normalmente se aplican a un único lenguaje de programación.

Los patrones más universales y de más alto nivel son los patrones de arquitectura. Los desarrolladores pueden implementar estos patrones prácticamente en cualquier lenguaje. Al contrario que otros patrones, pueden utilizarse para diseñar la arquitectura de una aplicación completa.

Además, todos los patrones pueden clasificarse por su propósito. Este libro cubre tres grupos generales de patrones:

* Los <strong>patrones creacionales</strong> proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización de código existente.

* Los <strong>patrones estructurales</strong>  explican cómo ensamblar objetos y clases en estructuras más grandes a la vez que se mantiene la flexibilidad y eficiencia de la estructura.

* Los <strong>patrones de comportamiento</strong>  se encargan de una comunicación efectiva y la asignación de responsabilidades entre objetos.

<a name="item3"></a>

## Patrones Creacionales

Proporcionan mecanismos de creacion de objetos, incrementando la flexibilidad y reutilización de código existente

<a name="Factory"></a>

### Factory
El patrón Factory Method define un método que debe utilizarse para crear objetos, en lugar de una llamada directa al constructor (operador new). Las subclases pueden sobrescribir este método para cambiar las clases de los objetos que se crearán.

Su implementación puede encontrarse en la carpeta [Factory](/Factory/).

<a name="AbstractFactory"></a>

### Abstract Factory
Abstract Factory es un patrón de diseño creacional que nos permite producir familias de objetos relacionados sin especificar sus clases concretas.

Su implementación puede encontrarse en la carpeta [AbstractFactory](/AbstractFactory/)

<a name="Builder"></a>

### Builder
Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.

Su implementación puede encontrarse en la carpeta [Builder](/Builder/)

<a name="Prototype"></a>

### Prototype 
El patrón Prototype es como tener una máquina que puede crear copias exactas de diferentes tipos de objetos sin necesidad de entender cómo se construyen. Imagina que tienes una herramienta mágica que puede duplicar cualquier objeto que se le presente. Esa es la esencia del patrón Prototype aplicado a la gestión de objetos en un sistema.

Su implementación puede encontrarse en la carpeta [Prototype](/Prototype/)


### Singleton

