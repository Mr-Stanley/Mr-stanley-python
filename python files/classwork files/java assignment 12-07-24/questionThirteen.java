import java.util.Scanner;
public class questionSixteen{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);
	
	int factorialNumber = 1;
	
	System.out.print("Enter a number: ");
	 int number = scanner.nextInt();
	
	for (int number1 = 1; number1 <= number; number1++){
		
		factorialNumber *= number1; 
		
			}
		
	System.out.print(factorialNumber);

}

}