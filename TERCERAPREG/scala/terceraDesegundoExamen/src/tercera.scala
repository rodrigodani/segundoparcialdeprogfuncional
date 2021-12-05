
object tercera {
   def main(args: Array[String]): Unit = {
    var a = Console.readLine();
    var sep = Console.readLine();
    dividir (a, sep)
   
    
  }
   def dividir (a:String, s: String) =
   {
     var l: Array[String] = a.split(s)
       
     for (x <-l)
     {
         println(x);
     }
     
   }
}