public class Operations{

    int[] array1 = {1,2,3,4,5};

    void PrintArray(){
        foreach(int i in array1){
            System.Console.WriteLine(i);
        }
    }

    void AddElement(int element){
        int[] newArray = new int[array1.Length + 1];
        for(int i = 0; i < array1.Length; i++){
            newArray[i] = array1[i];
        }
        newArray[array1.Length] = element;
        array1 = newArray;
    }

    void RemoveElement(int index){
        if(index < 0 || index >= array1.Length) return;
        int[] newArray = new int[array1.Length - 1];
        for(int i = 0, j = 0; i < array1.Length; i++){
            if(i != index){
                newArray[j++] = array1[i];
            }
        }
        array1 = newArray;
    }

    void getvalue(int index){
        if(index < 0 || index >= array1.Length) return;
        System.Console.WriteLine(array1[index]);
    }

    void getlength(){
        System.Console.WriteLine(array1.Length);    
     }



}