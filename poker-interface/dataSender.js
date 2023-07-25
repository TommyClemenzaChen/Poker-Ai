import axios from 'axios';


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
    

    if (res.status === 200) {
        console.log("Success");
    } else {
        console.log("Failure");
    }
    console.log(res.data["optimal_action"]);
    //showOptimalAction(res.data);
     
};

export default handleSubmit;
 
