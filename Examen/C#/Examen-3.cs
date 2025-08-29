using System;

public class comparar
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Por favor, Introduzca un numero: ");
        string entrada = Console.ReadLine();


        try
        {
            int num = Convert.ToInt32(entrada);

            if(num % 2 == 0){
                Console.WriteLine("El numero es par");

            }
            else{
                Console.WriteLine("El numero es impar");
            }
   
        }
        catch (FormatException)
        {
            Console.WriteLine("Error: Por favor, introduce solo números válidos.");
        }
    }
}