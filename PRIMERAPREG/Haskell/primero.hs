module Test where
-- This tells main to do nothing.
suma :: Int -> Int -> Int
suma a b = a + b;

resta :: Int -> Int -> Int
resta a b = a - b;

multip :: Int -> Int -> Int
multip a b = a * b;

divi :: Int -> Int -> Int
divi a b = a * b;

calculadora :: Int -> Int -> String -> Int
calculadora a b "suma" =  suma a b
calculadora a b "multi" =  multip a b  
calculadora a b "resta" =  resta a b
calculadora a b "divi" =  divi a b 

 
