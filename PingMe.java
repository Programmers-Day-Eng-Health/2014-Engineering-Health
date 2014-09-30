import java.net.HttpURLConnection;
import java.net.URL;
public class PingMe { 

    public static void main(String[] args) throws InterruptedException {
        while(!PingMe.checkIfURLExists(args[0])){
            Thread.sleep(5000);
        }
    }

    public static boolean checkIfURLExists(String targetUrl) {
        HttpURLConnection httpUrlConn;
        try {
            httpUrlConn = (HttpURLConnection) new URL(targetUrl).openConnection();
            httpUrlConn.setRequestMethod("HEAD");
            httpUrlConn.setConnectTimeout(30000);
            httpUrlConn.setReadTimeout(30000);
            System.out.println("Response Code: "+ httpUrlConn.getResponseCode());
            System.out.println("Response Message: "+ httpUrlConn.getResponseMessage());
            return (httpUrlConn.getResponseCode() == HttpURLConnection.HTTP_OK);
        } catch (Exception e) {
            System.out.println("Error: " + e.toString());
            return false;
        }
    }
}
