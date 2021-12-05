module Test where

dividir :: String -> [String]
dividir x = words x


split :: String -> [String]
split "" = []
split xs = [head xs] : split (tail xs)


 
