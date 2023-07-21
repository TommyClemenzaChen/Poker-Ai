import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import StarterPage from './StarterPage';
import customInput from './customInput';

const Stack = createStackNavigator();

const AppNavigator = () => {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="StarterPage"
        component={StarterPage}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="CustomInput"
        component={customInput}
        options={{ headerShown: false }}
      />
    </Stack.Navigator>
  );
};

export default AppNavigator;