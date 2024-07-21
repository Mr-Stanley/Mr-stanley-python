import java.util.Scanner;
public class question1 {
	public static void main(String []Args) {
	Scanner input = new Scanner(System.in);
int number = 0;
int counter = 0;
int oneNumber = 0;
int fails = 0;

	System.out.print("Enter an integer :");
	 oneNumber = input.nextInt();

	if (oneNumber != 1 && oneNumber != 2){
	counter = counter + 1;	}
	else 
   	fails += 1;



while (oneNumber != 1 && oneNumber != 2){
	
	System.out.print("Enter an integer :");
	 oneNumber = input.nextInt();
	

if (oneNumber != 1 && oneNumber != 2){
	counter = counter + 1;	}
else 
   	fails += 1;

	}
	System.out.println(fails);
	System.out.print(counter);
    }	
}	