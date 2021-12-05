

object segundo {
   def main(args: Array[String]): Unit = {
    var a= Console.readDouble();
    var b= Console.readDouble();
    var ope = Console.readLine();
    
    println(calcu(a, b, ope))   
  }
   val calcu = (a: Double, b: Double, ope: String)=>
   {
     ope  match {
      case "resta" => resta(a,b)
      case "suma" => suma(a,b)
      case "multip" => multi(a,b) 
      case "divi" => divi(a,b) 
    }
   }
   def resta = (a: Double, b: Double) =>a - b;
   def suma =(a: Double, b: Double) =>a + b;
   def multi =(a: Double, b: Double) =>a * b;
   def divi (a: Double, b: Double) =a / b;
}