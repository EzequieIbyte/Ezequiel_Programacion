using System;

public class SumadoraSimple
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Por favor, Introduzca un numero: ");
        string entrada1 = Console.ReadLine();

        Console.WriteLine("Por favor, Introduzca un numero: ");
        string entrada2 = Console.ReadLine();

        try
        {
            int num1 = Convert.ToInt32(entrada1);
            int num2 = Convert.ToInt32(entrada2);

            int suma = num1 + num2;

            Console.WriteLine($"La suma de {num1} y {num2} es: {suma}");
        }
        catch (FormatException)
        {
            Console.WriteLine("Error: Por favor, introduce solo números válidos.");
        }
    }
}