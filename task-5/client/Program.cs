using System; 
using System.Text;
// check whether all required namespaces are imported 
using System.Net;  
using System.Net.Sockets;  
  
public class SynchronousSocketClient {  
  
    public static void StartClient() {  
        // Data buffer for incoming data.  
        byte[] bytes = new byte[1024];  
  
        // Connect to a remote device.  
        try {  
            // Establish the remote endpoint for the socket.  
            // This example uses port 11000 on the local computer.  
            IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());  
            IPAddress ipAddress = ipHostInfo.AddressList[0];  
            IPEndPoint remoteEP = new IPEndPoint(ipAddress,11000);  
  
            // Check whether TCP Socket is created correctly
            Socket sender = new Socket(ipAddress.AddressFamily,
                SocketType.Stream, ProtocolType.Tcp );  
  
            // Connect the socket to the remote endpoint. Catch any errors.  
            try {  
                sender.Connect(remoteEP);  
                if (sender.RemoteEndPoint != null)  
                {  
                    Console.WriteLine("Socket connected to {0}",  
                        sender.RemoteEndPoint.ToString());  
                }  
                else  
                {  
                    Console.WriteLine("Socket not connected");  
                } 
                // check if the variable is defined correctly or not
                Console.WriteLine("Enter the person's name: ");
                string? name = Console.ReadLine();
                Console.WriteLine("Enter the person's interests: ");
                string? interests = Console.ReadLine();
                Console.WriteLine("Enter the person's Email: ");
                string? mail = Console.ReadLine();
                // Encode the data string into a byte array.  
                // check the data type of the data you are sending.
                byte[] msg = Encoding.ASCII.GetBytes(name + "," + interests + "," + mail+"<EOF>");  
  
                // Send the data through the socket.  
                int bytesSent = sender.Send(msg);  
  
                // Close the socket.  
                sender.Shutdown(SocketShutdown.Both);  
                sender.Close();  
  
            } catch (ArgumentNullException ane) {  
                Console.WriteLine("ArgumentNullException : {0}",ane.ToString());  
            } catch (SocketException se) {  
                Console.WriteLine("SocketException : {0}",se.ToString());  
            } catch (Exception e) {  
                Console.WriteLine("Unexpected exception : {0}", e.ToString());  
            }  
  
        } catch (Exception e) {  
            Console.WriteLine( e.ToString());  
        }  
    }  
    // check the main function
    public static int Main(String[] args) {  
        StartClient();  
        return 0;  
    }  
}