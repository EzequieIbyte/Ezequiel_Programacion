using System;

public class Recorrer
{

    public static void Main(string[] args){
        string[] diasSemana = { "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo" };
        
        
        foreach (string dia in diasSemana){
        Console.WriteLine(dia);
    }
    }

}