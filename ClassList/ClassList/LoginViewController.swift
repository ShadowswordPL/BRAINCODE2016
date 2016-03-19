//
//  LoginViewController.swift
//  ClassList
//
//  Created by Tomasz Bąk on 19.03.2016.
//  Copyright © 2016 Za Duzo Tomkow. All rights reserved.
//

import UIKit

class LoginViewController: UIViewController {
    @IBOutlet weak var username: UITextField!
    @IBOutlet weak var password: UITextField!
    @IBOutlet weak var indicator: UIActivityIndicatorView!
    @IBOutlet weak var loginButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
//        let background = UIImageView(image: UIImage(named: "background"))
//        navigationController?.view.addSubview(background)
//        navigationController?.view.sendSubviewToBack(background)
//        background.topAnchor.constraintEqualToAnchor(background.topAnchor)
//        background.bottomAnchor.constraintEqualToAnchor(background.bottomAnchor)
//        background.leftAnchor.constraintEqualToAnchor(background.leftAnchor)
//        background.rightAnchor.constraintEqualToAnchor(background.rightAnchor)
    }
    
    override func viewWillAppear(animated: Bool) {
        navigationController?.navigationBarHidden = true
    }
    
    @IBAction func login(sender: UIButton) {
        indicator.startAnimating()
        let delayTime = dispatch_time(DISPATCH_TIME_NOW, Int64(0.5 * Double(NSEC_PER_SEC)))
        dispatch_after(delayTime, dispatch_get_main_queue()) { [weak self] in
            self?.indicator.stopAnimating()
            self?.performSegueWithIdentifier("show classes", sender: nil)
        }
    }
    @IBAction func didTap(sender: UITapGestureRecognizer) {
        view.endEditing(false)
    }
    
    @IBAction func unwind(segue: UIStoryboardSegue) {
        
    }
}
