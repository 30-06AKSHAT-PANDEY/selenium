import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;

public class Main {
    public static void main(String[] args) {

        // Step 1: Setup driver
        WebDriver driver = new ChromeDriver();

        // Step 2: Open website
        driver.get("https://www.google.com");

        // Step 3: Find search box and type
        driver.findElement(By.name("q")).sendKeys("Selenium Java");

        // Step 4: Submit search
        driver.findElement(By.name("q")).submit();

        // Step 5: Close browser
        // driver.quit();
    }
}
