module Test where
-- This tells main to do nothing.
suma :: Int -> Int -> Int
suma = \a b -> a + b;

resta :: Int -> Int -> Int
resta = \a b -> a - b;

multip :: Int -> Int -> Int
multip = \a b -> a * b;

divi :: Int -> Int -> Int
divi = \a b -> a * b;

calculadora :: Int -> Int -> (String -> Int)
calculadora = \a b -> (\z -> if (z == "suma")then suma a b else if (z == "resta") then resta a b else if (z == "mult") then multip a b else divi a b)


 
