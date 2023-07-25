import * as React from "react";
import {Image, StyleSheet, Pressable, Text, View, TouchableOpacity} from "react-native";
import {useNavigation} from "@react-navigation/native";
import { FontFamily, Padding, Color, FontSize } from "./GlobalStyles";
import { useRoute} from "@react-navigation/native"
// import { TouchableOpacity } from "react-native-web";

const Result = () => {
	const navigation = useNavigation();
	

	const handleBackButton = () => {
		navigation.navigate("StudyPage"); 
	}
  	return (
    		<Pressable style={[styles.result, styles.iconLayout]} onPress={()=>{}}>
      			<View style={styles.header}>
						{/* back button */}
        				<TouchableOpacity style={[styles.back1, styles.backLayout]} onPress={handleBackButton}>
          					<Image style={[styles.icon, styles.iconLayout]} resizeMode="cover" source={require('./images/back.png')} />
        				</TouchableOpacity>
						{/* Title on the top of the page */}
        				<View style={[styles.textHereWrapper, styles.wrapperFlexBox]}>
          					<Text style={[styles.textHere2, styles.foldTypo]}>Result</Text>
        				</View>
        				<View style={[styles.back2, styles.backLayout]} />
      			</View>
				
      			<View style={[styles.frameParent, styles.buttonFlexBox]}>
        				<View style={[styles.frameWrapper, styles.wrapperFlexBox]}>
							{/* Text representing the result */}
          					<View style={styles.foldWrapper}>
            						<Text style={[styles.fold, styles.foldTypo]}>Fold</Text>
          					</View>
        				</View>
						{/*this is for result icons*/}
						<View>
							<Image 
							source={require("./images/fold_image.png")}
							style={{ width: 180, height: 180 }}
							// alt="Fold Image"
							/>
							
						</View>
						{/* Button to view explanation for hand, but we weren't able to implement*/}
        				<Pressable style={[styles.button, styles.emojiSpaceBlock]} onPress={()=>{}}>
          					<Text style={styles.textHere3}>View Details</Text>
        				</Pressable>
      			</View>
    		</Pressable>);
};

const styles = StyleSheet.create({
  	iconLayout: {
    		width: "100%",
    		overflow: "hidden"
  	},
  	backLayout: {
    		width: 48,
    		height: 48
  	},
  	wrapperFlexBox: {
    		justifyContent: "center",
    		alignItems: "center"
  	},
  	foldTypo: {
    		//fontFamily: FontFamily.plusJakartaSansBold,
    		fontWeight: "700",
    		textAlign: "left"
  	},
  	buttonFlexBox: {
    		paddingHorizontal: Padding.p_41xl,
    		justifyContent: "center",
    		alignItems: "center"
  	},
  	emojiSpaceBlock: {
    		marginTop: 60,
    		overflow: "hidden"
  	},
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
  	icon: {
    		height: "100%",
    		overflow: "hidden"
  	},
  	back1: {
    		height: 48
  	},
  	textHere2: {
    		color: Color.whitesmoke,
    		textAlign: "left",
    		fontSize: FontSize.size_lg
  	},
  	textHereWrapper: {
    		height: 48,
    		flexDirection: "row"
  	},
  	back2: {
    		height: 48,
    		overflow: "hidden"
  	},
  	header: {
    		borderColor: "#606060",
    		borderBottomWidth: 0.5,
    		width: 390,
    		height: 90,
    		alignItems: "flex-end",
    		justifyContent: "space-between",
    		flexDirection: "row",
    		borderStyle: "solid",
    		overflow: "hidden",
    		backgroundColor: Color.gray
  	},
  	fold: {
    		fontSize: 44,
    		color: Color.burlywood,
    		textAlign: "left"
  	},
  	foldWrapper: {
    		flexDirection: "row",
    		alignItems: "center"
  	},
  	frameWrapper: {
    		alignSelf: "stretch"
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
    		backgroundColor: Color.whitesmoke,
    		borderColor: "#252525",
    		borderWidth: 8,
    		width: 180,
    		height: 180,
    		borderStyle: "solid"
  	},
  	textHere3: {
    		fontWeight: "800",
    		//fontFamily: FontFamily.plusJakartaSansExtrabold,
    		color: Color.gray,
    		textAlign: "left",
    		fontSize: FontSize.size_lg
  	},
  	button: {
    		borderRadius: 30,
    		backgroundColor: Color.burlywood,
    		height: 60,
    		paddingVertical: 10,
    		paddingHorizontal: Padding.p_41xl,
    		justifyContent: "center",
    		alignItems: "center",
    		flexDirection: "row"
  	},
  	frameParent: {
    		paddingVertical: 80,
    		alignSelf: "stretch",
    		flex: 1
  	},
  	result: {
    		height: 844,
    		alignItems: "center",
    		overflow: "hidden",
    		flex: 1,
    		// backgroundColor: Color.gray
			backgroundColor: Color.gray_100
  	}
});

export default Result;
