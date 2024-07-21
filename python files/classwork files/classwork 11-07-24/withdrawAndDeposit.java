import java.util.Scanner;
public class withdrawAndDeposit{
	public static void main(String []Args) {
	Scanner input = new Scanner(System.in);
	
	
	int number = 0;
	int accountbalance = 0;
	int depositvalue = 0;
	int newaccountbalance = 0;
	int counter = 0;
	
while (number != 4){
	System.out.println("Welcome to Okoko Pos Terminal");
	System.out.printf("Select any of our services%n 1. Deposit%n 2. Withdraw%n 3. Check balance%n 4. Terminate :");
	 number = input.nextInt();

if (number == 1){
	System.out.print("Enter the amount you want to deposit");
		 depositvalue = input.nextInt();
		accountbalance = depositvalue + accountbalance;
	System.out.print("Your account balance is"+ accountbalance);

}
else if (number == 2){
	System.out.print("Enter the amount you want to withdraw");
			int withdrawalvalue = input.nextInt();
			if (withdrawalvalue < 0)
				System.out.println(" Thief!!! wetin you dey find");
	else if (withdrawalvalue > accountbalance){
		System.out.println("Insufficient Balance");
	}
	else accountbalance -= withdrawalvalue;
	
}
else if (number == 3){
	System.out.println("Your current account balance is "+ accountbalance);
}
else if (number == 4)
	System.out.print(" Thank You For Using Okoko Pos, See You Next Time");

}

	
	}


}	