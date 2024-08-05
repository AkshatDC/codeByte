{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cde01b2-db6d-4aca-a1ed-e936115f069e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "\n",
    "# Load the dataset\n",
    "file_path = 'input.csv'\n",
    "df = pd.read_csv(file_path)\n",
    "\n",
    "# Prepare the data with multiple features\n",
    "X = df[['MPA', 'Share of global plastics emitted to ocean', 'FisheryConsumption']]  \n",
    "y = df['MPA']\n",
    "\n",
    "# Initialize and train the Random Forest model\n",
    "rf = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "rf.fit(X, y)\n",
    "\n",
    "# Get feature importances\n",
    "importances = rf.feature_importances_\n",
    "\n",
    "# Create a DataFrame for plotting\n",
    "importances_df = pd.DataFrame({\n",
    "    'Feature': X.columns,\n",
    "    'Importance': importances\n",
    "}).sort_values(by='Importance', ascending=False)\n",
    "\n",
    "# Plot feature importances\n",
    "plt.figure(figsize=(10, 6))\n",
    "plt.bar(importances_df['Feature'], importances_df['Importance'])\n",
    "plt.xlabel('Feature')\n",
    "plt.ylabel('Importance')\n",
    "plt.title('Feature Importances from Random Forest')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2ae6de0-6b08-41c2-a559-c4160d012668",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
