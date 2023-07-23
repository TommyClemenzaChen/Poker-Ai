import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity , Icon } from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';
import Checkbox from 'expo-checkbox';
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';


const api = axios.create({
  baseURL: 'http://127.0.0.1:5000'
});
const handleSubmit = async (card1, card2, checked, position) => {
  const res = await api.post('/get_optimal_action', {
    card1_value: card1,
    card2_value: card2,
    are_suited: checked,
    player_name: 'bob',
    position: position,
    min_bet: 10,
  });
  console.log(res.data);
  showOptimalAction(res.data);

  if (res.status === 200) {
    console.log("Success");
  } else {
    console.log("Failure");
  }
};



const showOptimalAction = (action) => {
  alert(action["optimal_action"]);
};

const CustomInput = () => {

  const navigation = useNavigation(); 
  const [card1, setCard1] = React.useState('');
  const [card2, setCard2] = React.useState('');
  const [checked, checkTheBox] = React.useState(false);
  const [position, setPosition] = React.useState('');
  const positionData = ['SB', 'BB', '1', '2', '3', 'D'];
  
  const handleBackButton = () => {
    navigation.navigate("StarterPage"); 
  }
  const handlePress = () => {
    console.log('Submit');
    navigation.navigate("ResultPage");
    
    alert(
      data.find((item) => item.key === card1)?.value +
        "," +
        data.find((item) => item.key === card2)?.value +
        "\n" +
        position +
        "\n" +
        (checked ? "suited" : "not suited")
    );

    handleSubmit(card1, card2, checked, position);
  };



  const data = [
    { key: '1', value: 'A' },
    { key: '2', value: '2' },
    { key: '3', value: '3' },
    { key: '4', value: '4' },
    { key: '5', value: '5' },
    { key: '6', value: '6' },
    { key: '7', value: '7' },
    { key: '8', value: '8' },
    { key: '9', value: '9' },
    { key: '10', value: '10' },
    { key: '11', value: 'Jack' },
    { key: '12', value: 'Queen' },
    { key: '13', value: 'King' },
  ];

  return (
    <View style={styles.container}>

      <View style = {styles.heading}>
        <TouchableOpacity style={styles.backButton} onPress={handleBackButton}>
            <Text style={styles.backButtonText}>{"<"}</Text>
          </TouchableOpacity>

          <Text style={styles.title}>Study Mode</Text>
      </View>
      

      <View style={styles.inputContainer}>
        <View style={styles.cardInput}>
          <Text style={styles.cardInputTitle}>Select your cards</Text>

          <View style={styles.dropdownWrapper}>
            <View style={styles.dropdown}>
              <SelectList
                data={data}
                setSelected={setCard1}
                dropdownStyles={styles.dropdownStyles}
                placeholder="Select a card"
              />
            </View>

            <View style={styles.dropdown}>
              <SelectList
                data={data}
                setSelected={setCard2}
                dropdownStyles={styles.dropdownStyles}
                placeholder="Select a card"
              />
            </View>
          </View>
        </View>

        <View style={styles.checkboxContainer}>
          <Checkbox value={checked} onValueChange={checkTheBox} color="green" />
          <Text style={styles.checkboxText}>Suited</Text>
        </View>

        <View style={styles.positionContainer}>
          {positionData.map((pos, index) => (
            <TouchableOpacity
              key={index}
              style={[
                styles.positionButton,
                position === pos && styles.selectedPositionButton,
              ]}
              onPress={() => {
                setPosition(pos);
                console.log(pos);
              }}
            >
              <Text
                style={[
                  styles.positionButtonText,
                  position === pos && styles.selectedPositionButtonText,
                ]}
              >
                {pos}
              </Text>
            </TouchableOpacity>
          ))}
        </View>

        

        <TouchableOpacity style={styles.submitButton} onPress={handlePress}>
          <Text style={styles.submitButtonText}>Submit</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#171717',
    
  },
  inputContainer: {
    backgroundColor: 'gray',
    borderRadius: 20,
    padding: 20,
    marginHorizontal: 20,
    marginVertical: 40,
  },
  cardInput: {
    marginBottom: 20,
  },
  cardInputTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  dropdownWrapper: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  dropdown: {
    backgroundColor: 'gray',
    borderRadius: 10,
  },
  dropdownStyles: {
    backgroundColor: 'gray',
  },
  checkboxContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  checkboxText: {
    fontSize: 16,
    fontWeight: 'bold',
    marginLeft: 10,
  },
  positionContainer: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginBottom: 20,
  },
  positionButton: {
    backgroundColor: 'gray',
    borderRadius: 20,
    paddingVertical: 10,
    paddingHorizontal: 20,
    marginHorizontal: 5,
  },
  selectedPositionButton: {
    backgroundColor: 'green',
  },
  positionButtonText: {
    fontSize: 16,
    fontWeight: 'bold',
  },
  selectedPositionButtonText: {
    color: 'white',
  },
  backButton: {
    backgroundColor: '#171717',
    borderRadius: 10,
    width: 40,
    height: 40,

    alignSelf: 'left',
    justifyContent: 'center',
    
  },
  backButtonText: {
    fontSize: 25,
    fontWeight: 'bold',
    textAlign: 'center',
    color: 'white',
    
  },
  submitButton: {
    backgroundColor: 'green',
    borderRadius: 20,
    paddingVertical: 15,
    paddingHorizontal: 30,
    alignSelf: 'center',
  },
  submitButtonText: {
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
    color: 'white',
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    color: 'white',
    textAlign: 'center',
    marginLeft: 65,
    
  }, 
  heading: {
    flexDirection: 'row',
    marginTop: 40,
    marginBottom: 50,
    //justifyContent: 'space-between',
  }
  

});

export default CustomInput;