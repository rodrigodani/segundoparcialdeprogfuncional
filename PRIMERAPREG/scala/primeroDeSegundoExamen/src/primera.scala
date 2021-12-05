

object primera {
   def main(args: Array[String]): Unit = {
    var a= Console.readDouble();
    var b= Console.readDouble();
    var ope = Console.readLine();
    
    println(calcu(a, b, ope))   
  }
   def calcu (a: Double, b: Double, ope: String): Double =
   {
     ope  match {
      case "resta" => return resta(a,b)
      case "suma" => return suma(a,b)
      case "multip" => return multi(a,b) 
      case "divi" => return divi(a,b) 
    }
   }
   def resta (a: Double, b: Double): Double =
   {
     a - b;
   }
   def suma (a: Double, b: Double): Double =
   {
     a + b;
   }
   def multi (a: Double, b: Double): Double =
   {
     a * b;
   }
   def divi (a: Double, b: Double): Double =
   {
     a / b;
   }
}