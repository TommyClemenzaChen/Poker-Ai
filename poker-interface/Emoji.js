import * as React from "react";
import {Image, StyleSheet, View} from "react-native";

const Emoji = () => {
  	
  	return (
    		<View style={styles.emoji}>
      			<Image style={[styles.emojiChild, styles.emojiLayout]} resizeMode="cover" source="Polygon 1.png" />
      			<Image style={[styles.emojiItem, styles.emojiItemPosition]} resizeMode="cover" source="Polygon 2.png" />
      			<View style={[styles.vectorParent, styles.emojiItemPosition]}>
        				<Image style={[styles.vectorIcon, styles.vectorIconLayout]} resizeMode="cover" source="Vector.png" />
        				<Image style={[styles.vectorIcon1, styles.vectorIconLayout]} resizeMode="cover" source="Vector.png" />
        				<Image style={styles.frameChild} resizeMode="cover" source="Line 4.png" />
      			</View>
    		</View>);
};

const styles = StyleSheet.create({
  	emojiLayout: {
    		height: 79,
    		width: 22
  	},
  	emojiItemPosition: {
    		top: 91,
    		position: "absolute"
  	},
  	vectorIconLayout: {
    		height: 93,
    		width: 40
  	},
  	emojiChild: {
    		top: 90,
    		left: 50,
    		position: "absolute"
  	},
  	emojiItem: {
    		left: 108,
    		height: 79,
    		width: 22
  	},
  	vectorIcon: {
    		zIndex: 0
  	},
  	vectorIcon1: {
    		zIndex: 1,
    		marginLeft: 30
  	},
  	frameChild: {
    		top: 25,
    		left: 35,
    		width: 24,
    		height: 11,
    		zIndex: 2,
    		position: "absolute"
  	},
  	vectorParent: {
    		marginLeft: -47,
    		left: "50%",
    		flexDirection: "row"
  	},
  	emoji: {
    		borderRadius: 100,
    		backgroundColor: "#f0f0f0",
    		borderStyle: "solid",
    		borderColor: "#252525",
    		borderWidth: 8,
    		flex: 1,
    		width: "100%",
    		height: 180,
    		overflow: "hidden"
  	}
});

export default Emoji;
