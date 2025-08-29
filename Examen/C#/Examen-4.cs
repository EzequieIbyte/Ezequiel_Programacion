using System;

public class programa
{

    public static void saludar(string nombre){
        Console.WriteLine($"Hola,{nombre}");

    }

    public static void Main(string[] args){
        saludar("Daniel");
    }
}