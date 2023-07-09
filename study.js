import React from 'react';
import { View, Text, StyleSheet} from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';

import Checkbox from 'expo-checkbox';

const customInput = () => {
  
  const [selected, setSelected] = React.useState("")
  const [checked, checkTheBox] = React.useState(false)

  //Possible inputs for drop down box
  const data = [
    {key: '1', value: 'A'},
    {key: '2', value: '2'},
    {key: '3', value: '3'},
    {key: '4', value: '4'},
    {key: '5', value: '5'},
    {key: '6', value: '6'},
    {key: '7', value: '7'},
    {key: '8', value: '8'},
    {key: '9', value: '9'},
    {key: '10', value: '10'},
    {key: '11', value: 'Jack'},
    {key: '12', value: 'Queen'},
    {key: '13', value: 'King'},
  ];

  return (
    <>
      <View style = {styles.container}>

        <View style = {{paddingHorizontal: 20, paddingVertical: 50, flex: 1}}>
          <Text style = {{fontSize: 20, fontWeight: 'bold', textAlign: 'center'}}>Select your cards</Text>
          <SelectList
            data = {data} 
            setSelected = {setSelected}
            dropdownStyles = {{backgroundColor: 'gray'}}
            placeholder = "Select a card"

          />

          <SelectList
            data = {data} 
            setSelected = {setSelected}
            dropdownStyles = {{backgroundColor: 'gray'}}
            placeholder = "Select a card"
          />
        </View> 
        <Text style={styles.checkBoxText}>Suited?</Text>

        <View style = {styles.checkBox}>
          <Checkbox
            //style = {styles.checkBox}
            value = {checked}
            
            onValueChange = {checkTheBox}
            
            
          />
          
        </View>      
      </View>
    </>


  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    
  },
  checkBox: {
    //flex: 1,
    width: 24,
    height: 24,
    justifyContent: 'center',
    alignItems: 'center',
    textAlign : 'center',
    borderRadius: 4,
    borderWidth: 2,
    borderColor: 'coral',
    backgroundColor: 'transparent',
    marginBottom: 450,
    marginLeft: 150,

    
  },
  checkBoxText: {
    //flex: 1,
    backgroundColor: 'white',
    justifyContent: 'center',
    alignItems: 'center',
    //textAlign: 'center',
    fontSize: 16,
    fontWeight: 'bold',
    //marginBottom: 8,
  
  }

})
export default customInput;


