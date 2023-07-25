import React from 'react';
import { View, Text, TouchableOpacity, ImageBackground, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';

const StarterPage = () => {
  const navigation = useNavigation();

  const handlePlayButton = () => {
    navigation.navigate('StudyPage');
  };

  return (
    <View style={styles.container}>
      <View style={styles.borderTop} />
      <View style={styles.borderLeft} />
      <View style={styles.borderRight} />
      <View style={styles.borderBottom} />

      <ImageBackground
        source={require('./assets/chip.png')} // Replace with the path to your poker chip PNG file
        style={styles.button}
        resizeMode="contain"
        onPress={handlePlayButton}
      >
        <Text style={styles.buttonText}>Play</Text>
      </ImageBackground>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'gray',
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 50,
    fontFamily: 'Snell Roundhand',
    color: '#ff6060', 
    marginBottom: 50,
  },
  
  button: {
    width: 150,
    height: 150,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonText: {
    color: 'red',
    fontSize: 18,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  borderTop: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    height: 10,
    backgroundColor: '#ff6eff', // Neon pink color
  },
  borderLeft: {
    position: 'absolute',
    top: 0,
    left: 0,
    bottom: 0,
    width: 10,
    backgroundColor: '#ff6eff', // Neon pink color
  },
  borderRight: {
    position: 'absolute',
    top: 0,
    right: 0,
    bottom: 0,
    width: 10,
    backgroundColor: '#ff6eff', // Neon pink color
  },
  borderBottom: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    height: 10,
    backgroundColor: '#ff6eff', // Neon pink color
  },
});

export default StarterPage;
