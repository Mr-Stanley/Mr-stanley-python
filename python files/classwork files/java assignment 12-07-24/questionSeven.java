public class questionSeven{
public static void main(String...args){

	int square1 = 0;
	int cube1 = 0;

	System.out.print("number  square   cube");
	
	for(int number = 0; number <= 5; number++){
		for (int square = 0; square <= 5; square++){
			for (int cube = 0; cube <= 5; cube++){
				 square1 = number * number;
				 cube1 = number * square1;
				
				
					}
		
			}
	System.out.printf("%n%5d%9d%7d%n", number, square1, cube1);
	
	}

}


}