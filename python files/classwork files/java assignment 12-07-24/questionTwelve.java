import java.util.Scanner;
public class questionTwelve{
public static void main(String...args){

	Scanner scanner = new Scanner(System.in);
	
	System.out.print("Enter five number: ");
	int number = scanner.nextInt();
	
	int value1 = number % 10;
	int value2 = number / 10;
	int value3 = value2 % 10;
	int value4 = value2 / 10;
	int value5 = value4 % 10;
	int value6 = value4 / 10;
	int value7 = value6 % 10;
	int value8 = value6 / 10;
	
	if (value1 == value8 && value3 == value7)
			System.out.printf("This %d is a palindrome", number);
	else 
		System.out.printf("This %d is not palindrome", number);
	




}





}