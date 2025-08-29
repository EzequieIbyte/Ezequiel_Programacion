using System;

public class Tabla
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Por favor, Introduzca un numero: ");
        string entrada = Console.ReadLine();

   

        try
        {
            int num = Convert.ToInt32(entrada);

            for (int i = 1; i <= 10; i++){

                int resultado = num * i;
                Console.WriteLine($"{num} X {i} = {resultado}");
            }
   
        }
        catch (FormatException)
        {
            Console.WriteLine("Error: Por favor, introduce solo números válidos.");
        }
    }
}