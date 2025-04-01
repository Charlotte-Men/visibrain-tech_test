import axios from "axios";

const API_BASE_URL = "http://localhost:8000";

export const fetchVideosByGame = async (gameName) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/videos/`, {
      params: { game_name: gameName },
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching videos:", error);
    return [];
  }
};