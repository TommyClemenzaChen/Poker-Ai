// importing the necessary libraries and components
import React, {useState} from 'react';
import { Image, Pressable, View, Text, StyleSheet, TouchableOpacity , Icon} from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';
import { Color, FontFamily, FontSize, Padding, Border } from "./GlobalStyles";

// React component for the custom input
const CustomInput = () => {
  // hook to use naviation
  const navigation = useNavigation(); 
  // possible position in a poker game
  const positionData = ['BTN', 'Small Blind', 'Big Blind', 'UTG', 'Hijack', 'Cut-off'];
  // API instance creation
  const api = axios.create({
    baseURL: 'http://127.0.0.1:5000'
  });
  // Function to send a POST request to the server and handle the response
  const handleSubmit = async (card1, card2, checked, position) => {
    // Send POST request
    const res = await api.post('/get_optimal_action', {
      card1_value: card1,
      card2_value: card2,
      are_suited: checked,
      player_name: 'Bob',
      position: position,
      min_bet: 10,
    });
    // Check the status of the response
    if (res.status === 200) {
      console.log("Success");
    } else {
      console.log("Failure");
    }
    // Navigate to different pages based on the received data
    if(res.data["optimal_action"] === "FOLD"){
      navigation.navigate("FoldPage");
    }else{
      navigation.navigate("RaisePage");
    }
  };
  // Function to navigate back to the starting page
  const handleBackButton = () => {
    navigation.navigate("StarterPage"); 
  }
  // Function to submit user input
  const handlePress = async() => {
    // console.log('Submit');
    // console.log(data[selectedCard1-1].value);
    // console.log(data[selectedCard2-1].value);
    // console.log(suited);
    // console.log(positionData[lastPressedButton-1]);
    handleSubmit(data[selectedCard1-1].value, data[selectedCard2-1].value, suited, positionData[lastPressedButton-1]);
  };
  // List of cards
  const data = [
    { key: '1', value: 'A' },
    { key: '2', value: 'K' },
    { key: '3', value: 'Q' },
    { key: '4', value: 'J' },
    { key: '5', value: '10' },
    { key: '6', value: '9' },
    { key: '7', value: '8' },
    { key: '8', value: '7' },
    { key: '9', value: '6' },
    { key: '10', value: '5' },
    { key: '11', value: '4' },
    { key: '12', value: '3' },
    { key: '13', value: '2' },
  ];
  // useState hooks to handle checkbox states
  const [suited, setSuited] = useState(false);
  // Function to toggle suited checkbox
  const handleSuited = () => {
    setSuited(!suited);
  }
  // Variable to store color based on suited status
  const suitedColor = suited ? '#8DD2C5' : '#F0F0F0';
  // Variable to store image source based on suited status
  const imageSource = suited 
      ? require('./images/checked.png') 
      : require('./images/unchecked.png');
  
  // useState hooks to handle dropdown selection
  const [dropdown1Selected, setDropdown1] = useState("");
  // useState hook to handle button press
  const [lastPressedButton, setLastPressedButton] = useState(null);

  // Function to handle position button press
  const handlePress_position = (buttonNumber) => {
      setLastPressedButton(buttonNumber);
      // Enable the "VIEW PREFLOP ADVICE" button if the conditions are met
      if ([1, 2, 3, 4, 5, 6].includes(buttonNumber)) {
        if (selectedCard1 !== "" && selectedCard2 !== "") {
          setViewButtonEnabled(true);
        } else {
          setViewButtonEnabled(false);
        }
      } else {
        setViewButtonEnabled(false);
      }
  };
  
  // useState hook for enabling/disabling the view button
  const [isViewButtonEnabled, setViewButtonEnabled] = useState(false);
  // Determine color based on button enabled state
  const string_color = isViewButtonEnabled ? "#f0f0f0" : "#898989";

  // Dropdown configuration
  const dropdownItemHeight = 40; // Set this to the height of your dropdown items
  const maxDropdownHeight = 400; // Maximum dropdown height

  // Set dropdown minWidth and maxWidth
  const minWidth = 120;
  const maxWidth = 200;

  // Calculate dropdown height based on data length
  const dropdownHeight = Math.min(data.length * dropdownItemHeight, maxDropdownHeight);

  // useState hooks to handle card selection
  const [selectedCard1, setSelectedCard1] = useState("");
  const [selectedCard2, setSelectedCard2] = useState("");
  // Check if both cards are the same
  const areCardsSame = selectedCard1 === selectedCard2;
  // Button style based on card and suited status
  const disabledButtonStyle = areCardsSame ? {backgroundColor: '#898989'} : {backgroundColor: suitedColor};
  
// Begin the return statement of your component
return (
    <View style={[styles.studyMode, styles.headerBg]}>
      <View style={[styles.header, styles.headerFlexBox]}>
          {/* This TouchableOpacity navigates to the previous page when pressed. */}
          <TouchableOpacity style={[styles.back1, styles.backLayout]} onPress={handleBackButton}>
                {/* Image component that shows the back icon. */}
          		  <Image style={[styles.icon, styles.iconLayout]} resizeMode="cover" source={require('./images/back.png')} />
        	</TouchableOpacity>
          <View style={[styles.textHereWrapper, styles.parentFlexBox]}>
              {/* Text component that displays 'Study Mode' */}
              <Text style={[styles.textHere1, styles.card1Typo]}>Study Mode</Text>
          </View>
          <View style={styles.backIcon1} />
      </View>
    {/* A View component that holds some cards and other interactive elements. */}
    <View style={[styles.frameParent, styles.parentFlexBox]}>
        <View style={[styles.selectYourCardsParent, styles.parentFlexBox]}>
            <Text style={[styles.selectYourCards1, styles.card1Typo]}>Select Your Cards</Text>
            {/* View that contains dropdowns for card selection and a button to select if cards are suited. */}
            <View style={[styles.cardDropdownParent, styles.suitedButtonSpaceBlock]}>
            {/* Two SelectList components that allow the user to select cards.
            When a card is selected, it checks if both cards are selected and the last button was pressed. If so, it enables the View button. */}
            <SelectList 
                    setSelected={(val) => {
                          setSelectedCard1(val);
                          if(val !== "" && selectedCard2 !== "" && lastPressedButton) setViewButtonEnabled(true);
                          else setViewButtonEnabled(false);
                      }} 
                    data={data} 
                    placeholder="Card 1"
                    search={false}
                    maxHeight={250} 
                    boxStyles={{backgroundColor : "#f0f0f0", minWidth, maxWidth, paddingVertical: 16}}
                    inputStyles={{color:"#017A63", fontSize: 18, fontWeight: 700}}
                    dropdownTextStyles={{color: "#017A63", fontSize: 18, fontWeight: 700}}
                    dropdownStyles={{backgroundColor: "#f0f0f0", minWidth, maxWidth}}
                />
                <SelectList 
                    setSelected={(val) => {
                        setSelectedCard2(val);
                        if(val !== "" && selectedCard1 !== "" && lastPressedButton) setViewButtonEnabled(true);
                        else setViewButtonEnabled(false);
                    }} 
                    data={data} 
                    placeholder="Card 2"
                    search={false}
                    maxHeight={250} 
                    boxStyles={{backgroundColor : "#f0f0f0", minWidth, maxWidth, paddingVertical: 16}}
                    inputStyles={{color:"#017A63", fontSize: 18, fontWeight: 700}}
                    dropdownTextStyles={{color: "#017A63", fontSize: 18, fontWeight: 700}}
                    dropdownStyles={{backgroundColor: "#f0f0f0", minWidth, maxWidth}}
                />
            </View>
            {/* A TouchableOpacity component that handles the 'Suited' button. It is disabled if the selected cards are the same. */}
            <TouchableOpacity style={[styles.suitedButton, styles.cardDropdownFlexBox, disabledButtonStyle]} onPress={handleSuited} disabled={areCardsSame}>
                <Text style={[styles.card1, styles.card1Typo]}>Suited</Text>
                <Image style={styles.suitedButtonChild} resizeMode="cover" source={imageSource}/>
            </TouchableOpacity>
        </View>
        {/* A View component that asks the user about their position. */}
        <View style={[styles.whatsYourPositionParent, styles.parentFlexBox]}>
            <Text style={[styles.selectYourCards1, styles.card1Typo]}>What’s Your Position?</Text>
                {/* A series of TouchableOpacities that each represent a player's position. */}
                <View style={[styles.cardDropdownParent, styles.suitedButtonSpaceBlock]}>
                    <TouchableOpacity style={[lastPressedButton === 1 ? styles.coloredPlayer : styles.player, styles.playerSpaceBlock]} onPress={() => handlePress_position(1)}>
                        <Text style={[styles.card1, styles.card1Typo]}>D</Text>
                    </TouchableOpacity>
                    <View style={styles.frameGroup}>
                        <View style={[styles.playerGroup, styles.headerFlexBox]}>
                            <TouchableOpacity style={[lastPressedButton === 2 ? styles.coloredPlayer : styles.player, styles.playerSpaceBlock]} onPress={() => handlePress_position(2)}>
                                <Text style={[styles.card1, styles.card1Typo]}>SB</Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={[lastPressedButton === 3 ? styles.coloredPlayer : styles.player, styles.playerSpaceBlock]} onPress={() => handlePress_position(3)}>
                                <Text style={[styles.card1, styles.card1Typo]}>BB</Text>
                            </TouchableOpacity>
                        </View>
                        {/* A TouchableOpacity that leads to pre-flop advice. It is disabled if the 'View' button isn't enabled. */}
                        <TouchableOpacity 
                            style={[styles.viewButton, styles.viewSpaceBlock, !isViewButtonEnabled && styles.disabledButton]}
                            onPress={handlePress}
                            disabled={!isViewButtonEnabled}
                        >
                            <Text 
                              style={[styles.viewPreflopAdvice, {color: string_color}]}
                            >VIEW PREFLOP ADVICE
                            </Text>
                        </TouchableOpacity>
                        {/* A series of TouchableOpacities that each represent a player's position. */}
                        <View style={[styles.frameView, styles.viewSpaceBlock]}>
                        <TouchableOpacity style={[lastPressedButton === 4 ? styles.coloredPlayer : styles.player, styles.playerSpaceBlock]} onPress={() => handlePress_position(4)}>
                            <Text style={[styles.card1, styles.card1Typo]}>3</Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={[lastPressedButton === 5 ? styles.coloredPlayer : styles.player, styles.playerSpaceBlock]} onPress={() => handlePress_position(5)}>
                            <Text style={[styles.card1, styles.card1Typo]}>2</Text>
                        </TouchableOpacity>
                        </View>
                    </View>
                    <TouchableOpacity style={[lastPressedButton === 6 ? styles.coloredPlayer : styles.player, styles.playerSpaceBlock]} onPress={() => handlePress_position(6)}>
                        <Text style={[styles.card1, styles.card1Typo]}>1</Text>
                    </TouchableOpacity>
                </View>
            </View>
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
   
  },
  
  headerBg: {
    backgroundColor: "#252525",
    overflow: "hidden"
    },
    headerFlexBox: {
    justifyContent: "space-between",
    flexDirection: "row"
    },
    parentFlexBox: {
    justifyContent: "center",
    alignItems: "center"
    },
    card1Typo: {
    textAlign: "left",
    //FontFamily: "Times New Roman",
    fontWeight: "700"
    },
    suitedButtonSpaceBlock: {
    marginTop: 30,
    alignSelf: "stretch"
    },
    cardDropdownFlexBox: {
    paddingHorizontal: 24,
    borderRadius: 14,
    height: 60,
    backgroundColor: "#f0f0f0",
    justifyContent: "space-between",
    flexDirection: "row",
    alignItems: "center",
    overflow: "hidden"
    },
    playerSpaceBlock: {
    padding: 10,
    justifyContent: "center",
    overflow: "hidden"
    },
    viewSpaceBlock: {
    marginTop: 20,
    alignItems: "center"
    },
    backIcon1: {
    width: 48,
    height: 48,
    overflow: "hidden"
    },
    textHere1: {
    color: "#f0f0f0",
    fontSize: 18,
    textAlign: "left"
    },
    textHereWrapper: {
    height: 48,
    flexDirection: "row",
    justifyContent: "center"
    },
    header: {
    borderStyle: "solid",
    borderColor: "#606060",
    borderBottomWidth: 0.5,
    width: 390,
    height: 90,
    alignItems: "flex-end",
    overflow: "hidden",
    backgroundColor: "#252525"
    },
    selectYourCards1: {
    fontSize: 24,
    color: "#eabf6f"
    },
    card1: {
    color: "#017a63",
    fontSize: 18,
    textAlign: "left"
    },
    icroundArrowBackIosIcon2: {
    width: 16,
    height: 16,
    overflow: "hidden"
    },
    cardDropdown: {
    width: 160,
    paddingVertical: 8
    },
    cardDropdownParent: {
    justifyContent: "space-between",
    flexDirection: "row",
    alignItems: "center"
    },
    suitedButtonChild: {
    width: 24,
    height: 24
    },
    suitedButton: {
    paddingVertical: 10,
    marginTop: 30,
    alignSelf: "stretch",
    backgroundColor: '#F0F0F0'
    },
    selectYourCardsParent: {
    alignSelf: "stretch"
    },
    player: {
    borderRadius: 100,
    width: 60,
    height: 60,
    backgroundColor: "#f0f0f0",
    padding: 10,
    alignItems: "center"
    },
    coloredPlayer: {
      borderRadius: 100,
      width: 60,
      height: 60,
      backgroundColor: "#8DD2C5",
      padding: 10,
      alignItems: "center"
    },
    playerGroup: {
    alignSelf: "stretch",
    alignItems: "center"
    },
    viewPreflopAdvice: {
    color: "#f0f0f0",
    textAlign: "center",
    //fontFamily: "Times New Roman",
    fontWeight: "700",
    fontSize: 18
    },
    disabledPreflopAdvice: {
      color: "#898989",
      textAlign: "center",
      //FontFamily: "Times New Roman",
      fontWeight: "700",
      fontSize: 18
      },
    disabledButton: {
      borderRadius: 60,
      backgroundColor: "#606060",
      width: 180,
      height: 140,
      padding: 10,
      justifyContent: "center",
      overflow: "hidden"
    },
    viewButton: {
    borderRadius: 60,
    backgroundColor: "#017A63",
    width: 180,
    height: 140,
    padding: 10,
    justifyContent: "center",
    overflow: "hidden"
    },
    frameView: {
    alignSelf: "stretch",
    justifyContent: "space-between",
    flexDirection: "row"
    },
    frameGroup: {
    alignItems: "center"
    },
    whatsYourPositionParent: {
    marginTop: 60,
    alignSelf: "stretch"
    },
    frameParent: {
    paddingHorizontal: 25,
    paddingVertical: 60,
    alignSelf: "stretch",
    flex: 1
    },
    studyMode: {
    width: "100%",
    height: 844,
    alignItems: "center",
    overflow: "hidden",
    flex: 1
    },
    back1: {
      height: 48
    },
    backLayout: {
      width: 48,
      height: 48
    },
    icon: {
      height: "100%",
      overflow: "hidden"
    },
    iconLayout: {
      width: "100%",
      overflow: "hidden"
    },
    card: {
      paddingVertical: Padding.p_sm,
      width: 160,
    },
    cardParent: {
      marginLeft: -80,
      top: 0,
      left: "50%",
      position: "absolute",
      overflow: "hidden",
    },
    dropdown1: {
      top: 120,
      left: 0,
      shadowColor: "rgba(0, 0, 0, 0.1)",
      shadowOffset: {
        width: 0,
        height: 5,
      },
      shadowRadius: 10,
    elevation: 10,
    shadowOpacity: 1,
    height: 330,
    zIndex: 3,
    position: "absolute",
    width: 160,
    backgroundColor: Color.whitesmoke,
    borderRadius: Border.br_sm,
  },
  cardFlexBox: {
    paddingHorizontal: Padding.p_5xl,
    backgroundColor: Color.whitesmoke,
    flexDirection: "row",
    alignItems: "center",
    overflow: "hidden",
  }
});
export default CustomInput;